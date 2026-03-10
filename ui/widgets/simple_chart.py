from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygonF, QFont
from PyQt5.QtWidgets import QWidget


class TrendChartWidget(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.series = {}
        self.setMinimumHeight(220)

    def set_series(self, series):
        self.series = series
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        bg = QColor("#f5f9ff")
        painter.fillRect(self.rect(), bg)

        painter.setPen(QPen(QColor("#c4d5e8"), 1))
        frame = self.rect().adjusted(8, 8, -8, -8)
        painter.drawRect(frame)

        painter.setPen(QPen(QColor("#27415f"), 1))
        painter.setFont(QFont("Microsoft YaHei", 9, QFont.Bold))
        painter.drawText(frame.adjusted(8, 6, -8, -8), Qt.AlignLeft | Qt.AlignTop, self.title)

        chart = frame.adjusted(10, 28, -10, -12)
        painter.setPen(QPen(QColor("#d5e2ef"), 1, Qt.DashLine))
        painter.drawLine(chart.left(), chart.bottom(), chart.right(), chart.bottom())
        painter.drawLine(chart.left(), chart.top(), chart.left(), chart.bottom())

        all_values = []
        for cfg in self.series.values():
            all_values.extend(cfg.get("values", []))

        if not all_values:
            return

        min_v = min(all_values)
        max_v = max(all_values)
        if max_v - min_v < 1e-6:
            max_v += 1
            min_v -= 1

        for _, cfg in self.series.items():
            values = cfg.get("values", [])
            if len(values) < 2:
                continue

            color = QColor(cfg.get("color", "#4f8dcf"))
            painter.setPen(QPen(color, 2))

            points = QPolygonF()
            n = len(values)
            for i, v in enumerate(values):
                x = chart.left() + (chart.width() * i / max(1, n - 1))
                y_ratio = (float(v) - min_v) / (max_v - min_v)
                y = chart.bottom() - chart.height() * y_ratio
                points.append(QRectF(x, y, 1, 1).center())
            painter.drawPolyline(points)

        legend_x = chart.left()
        legend_y = chart.top() + 4
        painter.setFont(QFont("Microsoft YaHei", 8))
        for name, cfg in self.series.items():
            color = QColor(cfg.get("color", "#4f8dcf"))
            painter.setPen(QPen(color, 6))
            painter.drawLine(legend_x, legend_y, legend_x + 12, legend_y)
            painter.setPen(QPen(QColor("#27415f"), 1))
            painter.drawText(legend_x + 16, legend_y + 4, name)
            legend_x += 88


class BarChartWidget(QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.values = {}
        self.colors = {}
        self.setMinimumHeight(220)

    def set_values(self, values, colors=None):
        self.values = values
        self.colors = colors or {}
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor("#f5f9ff"))

        painter.setPen(QPen(QColor("#c4d5e8"), 1))
        frame = self.rect().adjusted(8, 8, -8, -8)
        painter.drawRect(frame)

        painter.setPen(QPen(QColor("#27415f"), 1))
        painter.setFont(QFont("Microsoft YaHei", 9, QFont.Bold))
        painter.drawText(frame.adjusted(8, 6, -8, -8), Qt.AlignLeft | Qt.AlignTop, self.title)

        chart = frame.adjusted(12, 30, -12, -14)
        if not self.values:
            return

        labels = list(self.values.keys())
        data = [max(0, float(v)) for v in self.values.values()]
        max_v = max(data) if data else 1
        if max_v < 1:
            max_v = 1

        bar_width = chart.width() / max(1, len(data) * 1.6)
        gap = bar_width * 0.6
        x = chart.left() + gap

        painter.setFont(QFont("Microsoft YaHei", 8))
        for idx, v in enumerate(data):
            h = chart.height() * (v / max_v)
            rect = QRectF(x, chart.bottom() - h, bar_width, h)
            color = QColor(self.colors.get(labels[idx], "#5a8ab9"))
            painter.fillRect(rect, color)
            painter.setPen(QPen(QColor("#27415f"), 1))
            painter.drawText(QRectF(x - 20, chart.bottom() + 2, bar_width + 40, 16), Qt.AlignCenter, labels[idx])
            painter.drawText(QRectF(x - 20, chart.bottom() - h - 16, bar_width + 40, 14), Qt.AlignCenter, str(int(v)))
            x += bar_width + gap
