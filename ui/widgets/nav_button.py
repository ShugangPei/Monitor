from PyQt5.QtWidgets import QPushButton


class NavButton(QPushButton):
    def __init__(self, text, page_index, parent=None):
        super().__init__(text, parent)
        self.page_index = page_index
        self.setCheckable(True)
        self.setObjectName("NavButton")
