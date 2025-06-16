from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class VariableCard(QWidget):
    
    def __init__(self, var_name, info, main_window):
        super().__init__()
        self.var_name = var_name
        self.info = info
        self.main_window = main_window
        self._init_ui()

    def _init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(18)

        # 图标
        icon_label = QLabel()
        icon_label.setFixedWidth(26)
        if self.info["type"] == "Boolean":
            icon_label.setText("🔘")
        elif self.info["type"] in ["Float", "REAL"]:
            icon_label.setText("🔢")
        else:
            icon_label.setText("🔤")
        layout.addWidget(icon_label)

        # 名称和注释
        name_lab = QLabel(f"{self.info['comment']} ({self.var_name})")
        name_lab.setObjectName("VarCardName")
        layout.addWidget(name_lab, stretch=3)

        # 当前值
        self.value_lab = QLabel("N/A")
        self.value_lab.setObjectName("VarCardValue")
        self.value_lab.setMinimumWidth(80)
        layout.addWidget(self.value_lab, stretch=2)

        # 可写变量：操作控件
        if self.info["writable"]:
            if self.info["type"] == "Boolean":
                self.btn = QPushButton("开/关")
                self.btn.setCheckable(True)
                self.btn.clicked.connect(self._toggle_bool)
                layout.addWidget(self.btn)
            else:
                self.edit = QLineEdit()
                self.edit.setPlaceholderText("输入值")
                self.edit.setFixedWidth(100)
                layout.addWidget(self.edit)
                self.write_btn = QPushButton("写入")
                self.write_btn.clicked.connect(self._write_value)
                layout.addWidget(self.write_btn)
        else:
            layout.addStretch()

        self.setObjectName("VarCard")

    def set_value(self, value):
        """主窗口定时刷新变量值"""
        t = self.info["type"]
        if t in ["Float", "REAL"] and isinstance(value, (int, float)):
            self.value_lab.setText(f"{value:.4f}")
        elif t == "Boolean":
            self.value_lab.setText("ON" if value else "OFF")
            if hasattr(self, 'btn'):
                self.btn.setChecked(bool(value))
                # 高亮按钮以区分状态
                self.btn.setStyleSheet("background:#2ecc71;" if value else "background:#c0392b;")
        else:
            self.value_lab.setText(str(value))

    def _toggle_bool(self):
        # 布尔变量翻转
        current = self.btn.isChecked()
        success, msg = self.main_window.write_variable(self.var_name, current)
        if not success:
            QMessageBox.critical(self, "写入失败", msg)

    def _write_value(self):
        val_str = self.edit.text()
        t = self.info["type"]
        try:
            if t in ["Float", "REAL"]:
                value = float(val_str)
            elif t in ["Int16", "Int32", "UInt16"]:
                value = int(val_str)
            else:
                value = val_str
        except ValueError:
            QMessageBox.warning(self, "非法输入", "请输入正确的数字")
            return
        success, msg = self.main_window.write_variable(self.var_name, value)
        if not success:
            QMessageBox.critical(self, "写入失败", msg)
