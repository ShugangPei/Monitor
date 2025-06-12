# PLC OPC UA 上位机监控系统

## 项目简介

本项目为基于 Python + PyQt5 + opcua 的 PLC 上位机监控与控制系统，支持变量分组管理、卡片化美观展示、OPC UA 实时读写、分组导航等功能，适用于工业自动化现场数据采集与人机交互（HMI/SCADA）。

## 主要特性

- OPC UA 协议实时通讯（适配大部分 PLC/工业设备）
- 变量分组、卡片化美观展示
- 现代化主题风格（浅色/深色一键切换）
- 支持变量读写、状态指示、分组导航
- 支持打包为 Windows/Linux 单文件可执行程序

## 环境依赖

- Python 3.7+
- PyQt5
- opcua

可使用如下命令安装依赖：

```bash
pip install PyQt5 opcua
```

## 项目结构

```
your_project/
├── main.py                    # 主入口
├── ui/
│   ├── MainWindow.py          # 主窗口
│   └── VariableCard.py        # 变量卡片控件
├── data/
│   ├── opcua_handler.py       # OPC UA 通信与变量写读
│   └── plc_variables.py       # PLC 变量分组与配置
├── resources/
│   ├── modern.qss             # 现代浅色风格
│   └── dark.qss               # 暗黑风格
└── README.md
```

## 运行方法

1. **配置 PLC 变量和连接信息**

   编辑 `data/plc_variables.py`，填入你的 PLC 变量节点、分组、连接参数等。

2. **直接运行源码**

   ```bash
   python main.py
   ```

3. **打包为可执行程序**

   - 安装 PyInstaller

     ```bash
     pip install pyinstaller
     ```

   - 在项目根目录下执行（Windows 示例）：

     ```bash
     pyinstaller --onefile --noconsole --add-data "resources;resources" main.py
     ```

     打包完成后会在 `dist` 目录下生成 `main.exe`。

     - Linux/Mac 下 `--add-data` 要用冒号 `:`，即 `--add-data "resources:resources"`

   - 拷贝 `dist/main.exe` 到目标电脑即可直接运行，无需 Python 环境。

4. **主题切换**

   默认加载 `resources/modern.qss`，如需切换到暗黑主题，请编辑 `main.py`，将如下代码注释切换：

   ```python
   # app.setStyleSheet(open("resources/dark.qss", "r", encoding="utf-8").read())
   app.setStyleSheet(open("resources/modern.qss", "r", encoding="utf-8").read())
   ```

## 常见问题

- **变量未刷新/无法通讯**：请确认网络连通、PLC OPC UA 服务器开启、节点地址无误。
- **界面元素错位/乱码**：请确保字体、QSS 文件编码为 UTF-8，且资源文件完整。
- **打包后样式丢失**：确认 `--add-data` 参数正确，且目标电脑有对应资源目录。

## 联系与支持

如需定制、Bug 反馈或二次开发指导，请在本仓库提交 Issue。

---

> **声明：本项目为开源示范用途，实际工业场景使用请根据安全规范加固，谨防误操作！**
