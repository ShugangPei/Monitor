from collections import deque

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout

from ui.widgets.simple_chart import TrendChartWidget, BarChartWidget


class MonitorPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.o2_series = deque(maxlen=240)
        self.pressure_series = deque(maxlen=240)
        self.history_o2 = deque(maxlen=120)
        self.state_values = {"准备": 0, "风机": 0, "自动": 0, "手动": 0}
        self.alarm_counts = {"严重": 0, "一般": 0, "提示": 0}

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

        self.realtime_chart = TrendChartWidget("实时曲线")
        self.history_chart = TrendChartWidget("历史趋势")
        self.state_chart = BarChartWidget("状态分布")
        self.alarm_chart = BarChartWidget("报警统计")

        panel_layout.addWidget(self.realtime_chart, 0, 0)
        panel_layout.addWidget(self.history_chart, 0, 1)
        panel_layout.addWidget(self.state_chart, 1, 0)
        panel_layout.addWidget(self.alarm_chart, 1, 1)

        root.addWidget(panel, 1)

        self._redraw()

    def update_values(self, values):
        self.o2_series.append(self._num(values.get("AI_CHAMBER_O2_CONTENT_OUTPUT_LASER")))
        self.pressure_series.append(self._num(values.get("AI_CHAMBER_PRESSURE_OUTPUT_LASER")))
        self.history_o2.append(self._num(values.get("AI_CHAMBER_O2_CONTENT_OUTPUT_LASER")))

        self.state_values = {
            "准备": 1 if values.get("CNC_Ready") else 0,
            "风机": 1 if values.get("RECIRCULATING_FAN_ON_H") else 0,
            "自动": 1 if values.get("AUTO_TEST_MODE") else 0,
            "手动": 1 if values.get("MANUAL_TEST_MODE") else 0,
        }

        self._redraw()

    def update_alarm_stats(self, counts):
        self.alarm_counts = counts
        self._redraw()

    def _redraw(self):
        self.realtime_chart.set_series(
            {
                "O2 ppm": {"values": list(self.o2_series), "color": "#4fd1c5"},
                "舱压": {"values": list(self.pressure_series), "color": "#f6ad55"},
            }
        )

        self.history_chart.set_series(
            {
                "O2 历史": {"values": list(self.history_o2), "color": "#63b3ed"},
            }
        )

        self.state_chart.set_values(
            self.state_values,
            colors={"准备": "#68d391", "风机": "#63b3ed", "自动": "#f6ad55", "手动": "#fc8181"},
        )

        self.alarm_chart.set_values(
            self.alarm_counts,
            colors={"严重": "#e53e3e", "一般": "#dd6b20", "提示": "#3182ce"},
        )

    @staticmethod
    def _num(value):
        try:
            return float(value)
        except Exception:
            return 0.0
