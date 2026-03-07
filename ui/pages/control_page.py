from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget, QScrollArea

from data.plc_variables import GROUPED_VARIABLES, VARIABLES
from ui.widgets.variable_control_card import VariableControlCard


class ControlPage(QWidget):
    write_requested = pyqtSignal(str, object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cards = {}

        root = QVBoxLayout(self)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        title = QLabel("控制")
        title.setObjectName("PageTitle")
        root.addWidget(title)

        self.tabs = QTabWidget()
        root.addWidget(self.tabs, 1)

        for group_name, names in GROUPED_VARIABLES.items():
            container = QWidget()
            content_layout = QVBoxLayout(container)
            content_layout.setContentsMargins(8, 8, 8, 8)
            content_layout.setSpacing(8)

            for var_name in names:
                info = VARIABLES.get(var_name, {"comment": var_name, "type": "REAL", "writable": False})
                card = VariableControlCard(var_name, info)
                card.write_requested.connect(self.write_requested.emit)
                content_layout.addWidget(card)
                self.cards[var_name] = card

            content_layout.addStretch(1)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(container)
            self.tabs.addTab(scroll, group_name)

    def update_values(self, values):
        for var_name, value in values.items():
            card = self.cards.get(var_name)
            if card:
                card.set_value(value)
