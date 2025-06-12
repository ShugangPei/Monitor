import sys
from PyQt5.QtWidgets import QApplication
from ui.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 可切换为暗色/亮色主题
    # app.setStyleSheet(open("resources/dark.qss", "r", encoding="utf-8").read())
    app.setStyleSheet(open("resources/modern.qss", "r", encoding="utf-8").read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())