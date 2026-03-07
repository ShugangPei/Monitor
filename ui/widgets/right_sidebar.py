from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout


class RightSidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("RightSidebar")
        self.value_widgets = {}
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(12)

        title = QLabel("打印任务与关键参数")
        title.setObjectName("SidebarTitle")
        layout.addWidget(title)

        self.task_box = self._make_box("打印任务", [
            ("任务名称", "task_name", "当前任务"),
            ("任务状态", "task_status", "待机"),
            ("当前程序行", "task_line", "--"),
            ("机台模式", "task_mode", "--"),
            ("准备状态", "task_ready", "--"),
        ])
        layout.addWidget(self.task_box)

        self.process_box = self._make_box("工艺参数", [
            ("舱氧含量(ppm)", "o2_ppm", "--"),
            ("高精氧含量", "o2_high", "--"),
            ("低精氧含量", "o2_low", "--"),
            ("舱压", "chamber_pressure", "--"),
            ("滤芯压差", "filter_pressure", "--"),
            ("风机状态", "fan_state", "--"),
            ("铺粉速度(mm/s)", "spread_speed", "--"),
        ])
        layout.addWidget(self.process_box)

        self.axis_box = self._make_box("轴状态", [
            ("X 位置", "x_pos", "--"),
            ("Y 位置", "y_pos", "--"),
            ("Z 位置", "z_pos", "--"),
            ("A 位置", "a_pos", "--"),
            ("B 位置", "b_pos", "--"),
        ])
        layout.addWidget(self.axis_box)
        layout.addStretch(1)

    def _make_box(self, title, rows):
        frame = QFrame()
        frame.setObjectName("SidebarBox")
        box = QVBoxLayout(frame)
        box.setContentsMargins(10, 10, 10, 10)

        header = QLabel(title)
        header.setObjectName("SidebarBoxTitle")
        box.addWidget(header)

        grid = QGridLayout()
        grid.setHorizontalSpacing(8)
        grid.setVerticalSpacing(6)
        box.addLayout(grid)

        for idx, (label_text, key, default) in enumerate(rows):
            key_label = QLabel(label_text)
            key_label.setObjectName("SidebarKey")
            value_label = QLabel(str(default))
            value_label.setObjectName("SidebarValue")
            grid.addWidget(key_label, idx, 0)
            grid.addWidget(value_label, idx, 1)
            self.value_widgets[key] = value_label

        return frame

    def update_values(self, values):
        def set_key(key, value):
            if key in self.value_widgets:
                self.value_widgets[key].setText(str(value))

        set_key("task_status", values.get("CNCStatus", "--"))
        set_key("task_line", values.get("CNCSourceNo", "--"))
        set_key("task_mode", "自动" if values.get("CNC_MODE") else "手动")
        set_key("task_ready", "是" if values.get("CNC_Ready") else "否")

        set_key("o2_ppm", values.get("AI_CHAMBER_O2_CONTENT_OUTPUT_LASER", "--"))
        set_key("o2_high", values.get("AI_HP_O2_CONTENT_OUTPUT_LASER", "--"))
        set_key("o2_low", values.get("AI_LP_O2_CONTENT_OUTPUT_LASER", "--"))
        set_key("chamber_pressure", values.get("AI_CHAMBER_PRESSURE_OUTPUT_LASER", "--"))
        set_key("filter_pressure", values.get("AI_FILTER_ELEMENT_PRESSURE_OUTPUT", "--"))
        set_key("fan_state", "ON" if values.get("RECIRCULATING_FAN_ON_H") else "OFF")
        set_key("spread_speed", values.get("Z_MoveVel", "--"))

        set_key("x_pos", values.get("X_PosNow", "--"))
        set_key("y_pos", values.get("Y_PosNow", "--"))
        set_key("z_pos", values.get("Z_PosNow", "--"))
        set_key("a_pos", values.get("A_PosNow", "--"))
        set_key("b_pos", values.get("B_PosNow", "--"))
