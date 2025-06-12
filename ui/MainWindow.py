import os
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QTabWidget, QScrollArea, QStatusBar, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtCore import QTimer
from data.opcua_handler import OPCUAHandler
from data.plc_variables import GROUPED_VARIABLES, VARIABLES
from ui.VariableCard import VariableCard

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PLC OPC UA 智能监控台")
        self.setGeometry(100, 100, 1200, 900)

        self.opc_handler = OPCUAHandler()
        self.cards = {}  # {var_name: VariableCard}
        self.is_running = True

        self._init_ui()
        self._start_opcua()

    def _init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # 顶部Logo和标题
        header = QLabel("🛠️ 智能制造上位机监控平台")
        header.setObjectName("MainTitle")
        header.setStyleSheet("font-size: 28px; font-weight: bold; padding: 20px; color: #3498db;")
        main_layout.addWidget(header)

        # 分组 Tab
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # 每个分组一个 Tab，变量用卡片方式排列
        for group_name, var_names in GROUPED_VARIABLES.items():
            tab = QWidget()
            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            cards_widget = QWidget()
            cards_layout = QVBoxLayout(cards_widget)

            for var_name in var_names:
                card = VariableCard(var_name, VARIABLES[var_name], self)
                self.cards[var_name] = card
                cards_layout.addWidget(card)
            cards_layout.addStretch()
            scroll.setWidget(cards_widget)
            tab_layout = QVBoxLayout(tab)
            tab_layout.addWidget(scroll)
            self.tabs.addTab(tab, group_name)

        # 底部状态栏
        self.status_bar = QStatusBar()
        self.status_bar.showMessage("未连接")
        self.setStatusBar(self.status_bar)

        # 退出按钮
        exit_btn = QPushButton("退出系统")
        exit_btn.setObjectName("ExitButton")
        exit_btn.clicked.connect(self._on_exit)
        main_layout.addWidget(exit_btn)

    def _start_opcua(self):
        if self.opc_handler.connect():
            self.status_bar.showMessage("已连接")
            self.timer = QTimer()
            self.timer.timeout.connect(self._update_values)
            self.timer.start(500)  # 500ms 刷新
        else:
            QMessageBox.critical(self, "错误", "无法连接到 PLC，请检查网络或配置")
            self._on_exit()

    def _update_values(self):
        if not self.is_running:
            return
        values = self.opc_handler.read_values()
        if values:
            for var_name, value in values.items():
                if var_name in self.cards:
                    self.cards[var_name].set_value(value)
            self.status_bar.showMessage("已连接")
        else:
            self.status_bar.showMessage("连接中断")

    def write_variable(self, var_name, value):
        """供 VariableCard 调用，写入PLC变量"""
        return self.opc_handler.write_value(var_name, value)

    def _on_exit(self):
        self.is_running = False
        self.opc_handler.disconnect()
        self.close()