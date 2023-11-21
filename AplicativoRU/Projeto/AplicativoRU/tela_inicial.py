from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QPixmap
from PySide6.QtCore import Qt, QPoint

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Divisão Diagonal de Cores")
        self.setGeometry(100, 100, 600, 400)

        custom_widget = DiagonalColorWidget(self)
        self.setCentralWidget(custom_widget)

class DiagonalColorWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        yellow = QColor(255, 249, 130)  
        black = QColor(0, 0, 0)  
        white = QColor(255, 255, 255)  


        painter.setBrush(yellow)
        polygon_yellow = [
            QPoint(0, 0),
            QPoint(self.width(), 0),
            QPoint(self.width(), self.height()),
        ]
        painter.drawPolygon(polygon_yellow)

        painter.setBrush(black)
        polygon_black = [
            QPoint(0, 0),
            QPoint(0, self.height()),
            QPoint(self.width(), self.height()),
        ]
        painter.drawPolygon(polygon_black)

        square_size = 200
        painter.setBrush(white)
        painter.drawRect(
            (self.width() - square_size) // 2,
            (self.height() - square_size) // 2,
            square_size,
            square_size,
        )

        image_path = "simbolo ut.png"
        pixmap = QPixmap(image_path)

        painter.drawPixmap(
            (self.width() - square_size) // 2,
            (self.height() - square_size) // 2,
            square_size,
            square_size,
            pixmap.scaled(square_size, square_size, Qt.KeepAspectRatio),
        )
