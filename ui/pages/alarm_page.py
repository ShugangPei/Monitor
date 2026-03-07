from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)


class AlarmPage(QWidget):
    ack_all_requested = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.alarms = {}

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        title = QLabel("报警")
        title.setObjectName("PageTitle")
        root.addWidget(title)

        row = QHBoxLayout()
        self.stat_label = QLabel("活动报警: 0")
        row.addWidget(self.stat_label)

        self.ack_btn = QPushButton("确认全部")
        self.ack_btn.clicked.connect(self.ack_all)
        row.addWidget(self.ack_btn)
        row.addStretch(1)

        root.addLayout(row)

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["时间", "级别", "报警项", "状态", "确认"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        root.addWidget(self.table, 1)

    def set_alarms(self, alarms):
        self.alarms = alarms
        active = [a for a in alarms.values() if a.active]
        self.stat_label.setText(f"活动报警: {len(active)}")

        rows = sorted(active, key=lambda a: a.timestamp, reverse=True)
        self.table.setRowCount(len(rows))
        for r, item in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(item.timestamp.strftime("%H:%M:%S")))
            self.table.setItem(r, 1, QTableWidgetItem(item.level))
            self.table.setItem(r, 2, QTableWidgetItem(item.message))
            self.table.setItem(r, 3, QTableWidgetItem("活动" if item.active else "已清除"))
            self.table.setItem(r, 4, QTableWidgetItem("已确认" if item.acknowledged else "未确认"))
            for c in range(5):
                self.table.item(r, c).setForeground(Qt.red if item.level == "ERROR" else Qt.yellow)

    def ack_all(self):
        for alarm in self.alarms.values():
            if alarm.active:
                alarm.acknowledged = True
        self.set_alarms(self.alarms)

    def get_alarm_counts(self):
        counts = {"严重": 0, "一般": 0, "提示": 0}
        for alarm in self.alarms.values():
            if not alarm.active:
                continue
            if alarm.level == "ERROR":
                counts["严重"] += 1
            elif alarm.level == "WARNING":
                counts["一般"] += 1
            else:
                counts["提示"] += 1
        return counts
