from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar,
    QFrame,
    QFormLayout,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
)


class PrintPage(QWidget):
    write_requested = pyqtSignal(str, object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.values = {}

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        header = QLabel("打印")
        header.setObjectName("PageTitle")
        root.addWidget(header)

        top = QHBoxLayout()
        top.setSpacing(10)
        root.addLayout(top)

        task_panel = QFrame()
        task_panel.setObjectName("Panel")
        task_layout = QVBoxLayout(task_panel)
        task_layout.addWidget(QLabel("任务进度"))
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        task_layout.addWidget(self.progress)

        self.status_label = QLabel("状态: 待机")
        task_layout.addWidget(self.status_label)

        btn_row = QHBoxLayout()
        self.start_btn = QPushButton("开始")
        self.pause_btn = QPushButton("暂停")
        self.stop_btn = QPushButton("停止")
        self.start_btn.clicked.connect(lambda: self.write_requested.emit("CNC_Start", True))
        self.pause_btn.clicked.connect(lambda: self.write_requested.emit("CNC_Pause", True))
        self.stop_btn.clicked.connect(lambda: self.write_requested.emit("CNC_Stop", True))
        btn_row.addWidget(self.start_btn)
        btn_row.addWidget(self.pause_btn)
        btn_row.addWidget(self.stop_btn)
        task_layout.addLayout(btn_row)
        top.addWidget(task_panel, 2)

        param_panel = QFrame()
        param_panel.setObjectName("Panel")
        form = QFormLayout(param_panel)
        self.fan_speed = QLineEdit()
        self.spread_speed = QLineEdit()
        self.filter_set = QLineEdit()
        form.addRow("风速(%)", self.fan_speed)
        form.addRow("铺粉速度", self.spread_speed)
        form.addRow("滤芯压差设定", self.filter_set)

        write_btn = QPushButton("写入参数")
        write_btn.clicked.connect(self._write_params)
        form.addRow(write_btn)
        top.addWidget(param_panel, 1)

        queue_panel = QFrame()
        queue_panel.setObjectName("Panel")
        queue_layout = QVBoxLayout(queue_panel)
        queue_layout.addWidget(QLabel("打印任务队列"))
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["任务", "材料", "状态", "进度"])
        self.table.horizontalHeader().setStretchLastSection(True)
        queue_layout.addWidget(self.table)
        root.addWidget(queue_panel, 1)

        self._seed_rows()

    def _seed_rows(self):
        self.table.setRowCount(1)
        self.table.setItem(0, 0, QTableWidgetItem("当前任务"))
        self.table.setItem(0, 1, QTableWidgetItem("钛合金"))
        self.table.setItem(0, 2, QTableWidgetItem("待机"))
        self.table.setItem(0, 3, QTableWidgetItem("0%"))

    def _write_params(self):
        if self.spread_speed.text().strip():
            self.write_requested.emit("Z_MoveVel", self._to_float(self.spread_speed.text()))
        if self.filter_set.text().strip():
            self.write_requested.emit("AI_FILTER_ELEMENT_PRESSURE_SET_H", self._to_float(self.filter_set.text()))

    @staticmethod
    def _to_float(raw):
        try:
            return float(raw)
        except ValueError:
            return raw

    def update_values(self, values):
        self.values = values
        status = values.get("CNCStatus", "待机")
        line = values.get("CNCSourceNo", 0)

        progress = 0
        if isinstance(line, (int, float)):
            progress = int(max(0, min(100, line % 101)))

        self.progress.setValue(progress)
        self.status_label.setText(f"状态: {status} | 行号: {line}")
        fan_raw = values.get("RECIRCULATING_FAN_ON_H")
        self.fan_speed.setPlaceholderText("当前: ON" if fan_raw else "当前: OFF")
        self.spread_speed.setPlaceholderText(f"当前: {values.get('Z_MoveVel', '--')}")
        self.filter_set.setPlaceholderText(f"当前: {values.get('AI_FILTER_ELEMENT_PRESSURE_SET_H', '--')}")

        self.table.setItem(0, 2, QTableWidgetItem(str(status)))
        self.table.setItem(0, 3, QTableWidgetItem(f"{progress}%"))


