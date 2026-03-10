from collections import deque

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout

from ui.widgets.simple_chart import TrendChartWidget


class MonitorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.x_series = deque(maxlen=240)
        self.y_series = deque(maxlen=240)
        self.o2_series = deque(maxlen=240)
        self.chamber_pressure_series = deque(maxlen=240)
        self.filter_pressure_series = deque(maxlen=240)

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        title = QLabel("监控")
        title.setObjectName("PageTitle")
        root.addWidget(title)

        panel = QFrame()
        panel.setObjectName("Panel")
        panel_layout = QGridLayout(panel)
        panel_layout.setContentsMargins(10, 10, 10, 10)
        panel_layout.setSpacing(10)

        self.xy_chart = TrendChartWidget("X和Y轴位置变化")
        self.o2_chart = TrendChartWidget("工作腔氧含量值变化")
        self.chamber_pressure_chart = TrendChartWidget("工作腔压力值变化")
        self.filter_pressure_chart = TrendChartWidget("过滤系统风压反馈值变化")

        panel_layout.addWidget(self.xy_chart, 0, 0)
        panel_layout.addWidget(self.o2_chart, 0, 1)
        panel_layout.addWidget(self.chamber_pressure_chart, 1, 0)
        panel_layout.addWidget(self.filter_pressure_chart, 1, 1)

        root.addWidget(panel, 1)

        self._redraw()

    def update_values(self, values):
        self.x_series.append(self._num(values.get("X_PosNow")))
        self.y_series.append(self._num(values.get("Y_PosNow")))

        # 优先使用激光工况变量，缺失时回退到密封测试变量
        self.o2_series.append(
            self._num(self._pick(values, "AI_CHAMBER_O2_CONTENT_OUTPUT_LASER", "AI_CHAMBER_O2_CONTENT_OUTPUT_SEAL"))
        )
        self.chamber_pressure_series.append(
            self._num(self._pick(values, "AI_CHAMBER_PRESSURE_OUTPUT_LASER", "AI_CHAMBER_PRESSURE_OUTPUT_SEAL"))
        )
        self.filter_pressure_series.append(self._num(values.get("AI_FILTER_ELEMENT_PRESSURE_OUTPUT")))

        self._redraw()

    def update_alarm_stats(self, counts):
        # 与 MainWindow 调用保持兼容，本页不再显示报警统计图。
        return

    def _redraw(self):
        self.xy_chart.set_series(
            {
                "X_PosNow": {"values": list(self.x_series), "color": "#3e7cb5"},
                "Y_PosNow": {"values": list(self.y_series), "color": "#7a9e2b"},
            }
        )

        self.o2_chart.set_series(
            {
                "AI_CHAMBER_O2_CONTENT_OUTPUT": {"values": list(self.o2_series), "color": "#1f9d8b"},
            }
        )

        self.chamber_pressure_chart.set_series(
            {
                "AI_CHAMBER_PRESSURE_OUTPUT": {"values": list(self.chamber_pressure_series), "color": "#c26d2b"},
            }
        )

        self.filter_pressure_chart.set_series(
            {
                "AI_FILTER_ELEMENT_PRESSURE_OUTPUT": {"values": list(self.filter_pressure_series), "color": "#6b4f9b"},
            }
        )

    @staticmethod
    def _pick(values, primary, fallback):
        primary_value = values.get(primary)
        if primary_value is not None:
            return primary_value
        return values.get(fallback)

    @staticmethod
    def _num(value):
        try:
            return float(value)
        except Exception:
            return 0.0
