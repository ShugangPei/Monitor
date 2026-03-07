from datetime import datetime

from PyQt5.QtCore import QObject, QTimer, pyqtSignal, pyqtSlot

from data.opcua_handler import OPCUAHandler


class OPCUAWorker(QObject):
    connected = pyqtSignal(bool, str)
    values_updated = pyqtSignal(dict)
    write_finished = pyqtSignal(str, bool, str)
    heartbeat = pyqtSignal(datetime)

    def __init__(self, interval_ms=500):
        super().__init__()
        self.interval_ms = interval_ms
        self.handler = OPCUAHandler()
        self.timer = None
        self.running = False

    @pyqtSlot()
    def start(self):
        if self.running:
            return
        ok = self.handler.connect()
        self.connected.emit(ok, "连接成功" if ok else f"连接失败: {self.handler.last_error}")
        if not ok:
            return

        self.running = True
        self.timer = QTimer(self)
        self.timer.setInterval(self.interval_ms)
        self.timer.timeout.connect(self.poll)
        self.timer.start()

    @pyqtSlot()
    def poll(self):
        if not self.running:
            return
        values = self.handler.read_values()
        if values:
            self.values_updated.emit(values)
            self.heartbeat.emit(datetime.now())

    @pyqtSlot(str, object)
    def write_variable(self, var_name, value):
        success, message = self.handler.write_value(var_name, value)
        self.write_finished.emit(var_name, success, message)

    @pyqtSlot()
    def stop(self):
        self.running = False
        if self.timer:
            self.timer.stop()
            self.timer.deleteLater()
            self.timer = None
        self.handler.disconnect()
