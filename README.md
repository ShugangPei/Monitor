# SLM OPC UA 控制平台

基于 `Python + PyQt5 + opcua` 的工业控制上位机。

## 功能
- 五个主界面：打印、控制、监控、日志、报警。
- 全局右侧常驻栏：打印任务与关键参数（所有页面可见）。
- OPC UA 实时采集与写入，默认 500ms 刷新。
- 监控图表：实时曲线、历史趋势、状态分布、报警统计。
- 支持 1366x768 与高 DPI 显示。

## 目录结构
- `main.py`：程序入口。
- `ui/MainWindow.py`：主窗口与页面编排、报警规则。
- `ui/opcua_worker.py`：OPC UA 后台线程采集器。
- `ui/pages/`：五个业务页面。
- `ui/widgets/`：导航、变量卡片、右侧栏等复用组件。
- `data/opcua_handler.py`：OPC UA 连接与读写封装。
- `data/plc_variables.py`：PLC 节点与变量分组定义。
- `resources/control_theme.qss`：统一主题样式。

## 运行
```bash
pip install PyQt5 opcua
python main.py
```

## OPC UA 配置
在 `data/plc_variables.py` 修改：
- `PLC_URL`
- `USERNAME`
- `PASSWORD`
- `VARIABLES`（节点映射）
- `GROUPED_VARIABLES`（控制页分组）

## 说明
- 右侧常驻栏优先使用现有参数名映射；缺失字段显示占位值，后续可继续对齐你的最终参数表。
- 报警与日志当前全部由 PLC 实时值推导，不依赖本地数据库。
