from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
)


class LogPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logs = []

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        title = QLabel("日志")
        title.setObjectName("PageTitle")
        root.addWidget(title)

        filter_row = QHBoxLayout()
        filter_row.addWidget(QLabel("级别"))
        self.level_filter = QComboBox()
        self.level_filter.addItems(["全部", "INFO", "WARNING", "ERROR"])
        self.level_filter.currentTextChanged.connect(self.refresh)
        filter_row.addWidget(self.level_filter)

        filter_row.addWidget(QLabel("检索"))
        self.search = QLineEdit()
        self.search.setPlaceholderText("输入关键字")
        self.search.textChanged.connect(self.refresh)
        filter_row.addWidget(self.search, 1)

        root.addLayout(filter_row)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["时间", "级别", "来源", "内容"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        root.addWidget(self.table, 1)

    def add_log(self, log_entry):
        self.logs.append(log_entry)
        if len(self.logs) > 2000:
            self.logs = self.logs[-2000:]
        self.refresh()

    def refresh(self):
        level = self.level_filter.currentText()
        keyword = self.search.text().strip().lower()

        rows = []
        for item in self.logs:
            if level != "全部" and item.level != level:
                continue
            if keyword and keyword not in item.message.lower() and keyword not in item.source.lower():
                continue
            rows.append(item)

        self.table.setRowCount(len(rows))
        for r, item in enumerate(rows):
            self.table.setItem(r, 0, QTableWidgetItem(item.timestamp.strftime("%H:%M:%S")))
            self.table.setItem(r, 1, QTableWidgetItem(item.level))
            self.table.setItem(r, 2, QTableWidgetItem(item.source))
            self.table.setItem(r, 3, QTableWidgetItem(item.message))

            if item.level == "ERROR":
                for c in range(4):
                    self.table.item(r, c).setForeground(Qt.red)
            elif item.level == "WARNING":
                for c in range(4):
                    self.table.item(r, c).setForeground(Qt.yellow)
