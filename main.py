import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from ui.MainWindow import MainWindow


def _load_stylesheet() -> str:
    path = os.path.join(os.path.dirname(__file__), "resources", "control_theme.qss")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setStyleSheet(_load_stylesheet())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
