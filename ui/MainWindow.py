from datetime import datetime

from PyQt5.QtCore import QThread, pyqtSignal, Qt, QMetaObject
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QFrame,
    QStackedWidget,
    QButtonGroup,
    QStatusBar,
)

from ui.opcua_worker import OPCUAWorker
from ui.pages.alarm_page import AlarmPage
from ui.pages.control_page import ControlPage
from ui.pages.log_page import LogPage
from ui.pages.monitor_page import MonitorPage
from ui.pages.print_page import PrintPage
from ui.types import LogEntry, AlarmEntry
from ui.widgets.nav_button import NavButton
from ui.widgets.right_sidebar import RightSidebar


class MainWindow(QMainWindow):
    write_request = pyqtSignal(str, object)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("SLM 控制平台")
        self.resize(1600, 900)
        self.setMinimumSize(1280, 720)

        self.values = {}
        self.alarms = {}
        self.alarm_previous = {}

        self._build_ui()
        self._build_worker()

    def _build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        self.nav = self._build_nav()
        layout.addWidget(self.nav)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack, 1)

        self.sidebar = RightSidebar()
        self.sidebar.setMinimumWidth(300)
        self.sidebar.setMaximumWidth(360)
        layout.addWidget(self.sidebar)

        self.print_page = PrintPage()
        self.control_page = ControlPage()
        self.monitor_page = MonitorPage()
        self.log_page = LogPage()
        self.alarm_page = AlarmPage()

        self.stack.addWidget(self.print_page)
        self.stack.addWidget(self.control_page)
        self.stack.addWidget(self.monitor_page)
        self.stack.addWidget(self.log_page)
        self.stack.addWidget(self.alarm_page)

        self.print_page.write_requested.connect(self._request_write)
        self.control_page.write_requested.connect(self._request_write)

        self.status_bar = QStatusBar()
        self.status_bar.showMessage("未连接")
        self.setStatusBar(self.status_bar)

    def _build_nav(self):
        frame = QFrame()
        frame.setObjectName("NavFrame")
        frame.setMinimumWidth(160)
        frame.setMaximumWidth(180)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        title = QLabel("SLM 控制")
        title.setObjectName("NavTitle")
        layout.addWidget(title)

        self.nav_group = QButtonGroup(self)
        self.nav_group.setExclusive(True)

        pages = [
            ("打印", 0),
            ("控制", 1),
            ("监控", 2),
            ("日志", 3),
            ("报警", 4),
        ]

        for text, idx in pages:
            btn = NavButton(text, idx)
            btn.clicked.connect(lambda checked, i=idx: self.stack.setCurrentIndex(i))
            self.nav_group.addButton(btn)
            layout.addWidget(btn)

        first = self.nav_group.buttons()[0]
        first.setChecked(True)

        layout.addStretch(1)
        return frame

    def _build_worker(self):
        self.worker_thread = QThread(self)
        self.worker = OPCUAWorker(interval_ms=500)
        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.started.connect(self.worker.start)
        self.worker.connected.connect(self._on_connected)
        self.worker.values_updated.connect(self._on_values_updated)
        self.worker.write_finished.connect(self._on_write_finished)

        self.write_request.connect(self.worker.write_variable)
        self.worker_thread.start()

    def _request_write(self, var_name, value):
        self.write_request.emit(var_name, value)

    def _on_connected(self, ok, message):
        self.status_bar.showMessage(message)
        level = "INFO" if ok else "ERROR"
        self._log(level, "OPCUA", message)

    def _on_values_updated(self, values):
        self.values = values
        self.sidebar.update_values(values)
        self.print_page.update_values(values)
        self.control_page.update_values(values)
        self.monitor_page.update_values(values)

        self._evaluate_alarms(values)
        self.alarm_page.set_alarms(self.alarms)
        self.monitor_page.update_alarm_stats(self.alarm_page.get_alarm_counts())

    def _on_write_finished(self, var_name, success, message):
        self.status_bar.showMessage(message)
        self._log("INFO" if success else "ERROR", var_name, message)

    def _log(self, level, source, message):
        entry = LogEntry(
            timestamp=datetime.now(),
            level=level,
            source=source,
            message=message,
        )
        self.log_page.add_log(entry)

    def _evaluate_alarms(self, values):
        fan_on = bool(values.get("RECIRCULATING_FAN_ON_H"))
        self._set_alarm_state(
            key="fan_off",
            active=not fan_on,
            level="ERROR",
            message="风机未打开",
        )

        chamber_ok = bool(values.get("CHAMBER_O2_OK_LASER"))
        self._set_alarm_state(
            key="o2_not_ok",
            active=not chamber_ok,
            level="WARNING",
            message="舱氧含量未达标",
        )

        filter_p = self._to_num(values.get("AI_FILTER_ELEMENT_PRESSURE_OUTPUT"))
        filter_set = self._to_num(values.get("AI_FILTER_ELEMENT_PRESSURE_SET_H"))
        self._set_alarm_state(
            key="filter_pressure",
            active=filter_set > 0 and filter_p > filter_set,
            level="WARNING",
            message="过滤器滤芯压差超上限",
        )

        o2 = self._to_num(values.get("AI_CHAMBER_O2_CONTENT_OUTPUT_LASER"))
        self._set_alarm_state(
            key="o2_high",
            active=o2 >= 2500,
            level="ERROR",
            message="舱氧含量过高，建议停机检查",
        )

        ready = bool(values.get("CNC_Ready"))
        start = bool(values.get("CNC_Start"))
        self._set_alarm_state(
            key="start_without_ready",
            active=start and not ready,
            level="ERROR",
            message="设备未准备完成但收到启动信号",
        )

    def _set_alarm_state(self, key, active, level, message):
        previous_active = self.alarm_previous.get(key, False)

        if key not in self.alarms:
            self.alarms[key] = AlarmEntry(
                key=key,
                timestamp=datetime.now(),
                level=level,
                message=message,
                active=active,
                acknowledged=False,
            )
        alarm = self.alarms[key]
        alarm.level = level
        alarm.message = message

        if active and not previous_active:
            alarm.timestamp = datetime.now()
            alarm.active = True
            alarm.acknowledged = False
            self._log(level, "Alarm", message)
        elif not active and previous_active:
            alarm.active = False
            self._log("INFO", "Alarm", f"报警恢复: {message}")
        else:
            alarm.active = active

        self.alarm_previous[key] = active

    def closeEvent(self, event):
        if hasattr(self, "worker"):
            QMetaObject.invokeMethod(self.worker, "stop", Qt.BlockingQueuedConnection)
        if hasattr(self, "worker_thread"):
            self.worker_thread.quit()
            self.worker_thread.wait(2000)
        super().closeEvent(event)

    @staticmethod
    def _to_num(value):
        try:
            return float(value)
        except Exception:
            return 0.0


