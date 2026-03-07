from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)


class VariableControlCard(QWidget):
    write_requested = pyqtSignal(str, object)

    def __init__(self, var_name, info, parent=None):
        super().__init__(parent)
        self.var_name = var_name
        self.info = info
        self.setObjectName("VarCard")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(10)

        self.name_label = QLabel(f"{info.get('comment', var_name)} ({var_name})")
        self.name_label.setObjectName("VarCardName")
        layout.addWidget(self.name_label, 4)

        self.value_label = QLabel("--")
        self.value_label.setObjectName("VarCardValue")
        self.value_label.setMinimumWidth(120)
        layout.addWidget(self.value_label, 2)

        self.status_label = QLabel("只读" if not info.get("writable") else "可写")
        self.status_label.setObjectName("VarCardStatus")
        layout.addWidget(self.status_label, 1)

        self.bool_button = None
        self.edit = None
        self.write_btn = None

        if info.get("writable"):
            if info.get("type") == "Boolean":
                self.bool_button = QPushButton("切换")
                self.bool_button.setCheckable(True)
                self.bool_button.clicked.connect(self._toggle_bool)
                layout.addWidget(self.bool_button, 1)
            else:
                self.edit = QLineEdit()
                self.edit.setPlaceholderText("输入值")
                self.edit.setMaximumWidth(120)
                layout.addWidget(self.edit, 1)

                self.write_btn = QPushButton("写入")
                self.write_btn.clicked.connect(self._write_value)
                layout.addWidget(self.write_btn, 1)

    def set_value(self, value):
        t = self.info.get("type")
        if value is None:
            self.value_label.setText("--")
            return

        if t in ("Float", "REAL") and isinstance(value, (int, float)):
            self.value_label.setText(f"{value:.3f}")
        elif t == "Boolean":
            bool_val = bool(value)
            self.value_label.setText("ON" if bool_val else "OFF")
            if self.bool_button is not None:
                self.bool_button.setChecked(bool_val)
        else:
            self.value_label.setText(str(value))

    def _toggle_bool(self):
        if self.bool_button is None:
            return
        self.write_requested.emit(self.var_name, self.bool_button.isChecked())

    def _write_value(self):
        if self.edit is None:
            return

        raw = self.edit.text().strip()
        if not raw:
            return

        t = self.info.get("type")
        try:
            if t in ("Float", "REAL"):
                value = float(raw)
            elif t in ("Int16", "Int32", "UInt16"):
                value = int(raw)
            else:
                value = raw
            self.write_requested.emit(self.var_name, value)
        except ValueError:
            self.value_label.setText("输入错误")
