from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QPixmap
from PySide6.QtCore import Qt, QPoint

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Divisão Diagonal de Cores")
        self.setGeometry(100, 100, 600, 400)

        # Criar um widget personalizado
        custom_widget = DiagonalColorWidget(self)
        self.setCentralWidget(custom_widget)

class DiagonalColorWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Configurar cores
        yellow = QColor(255, 249, 130)  # Amarelo
        black = QColor(0, 0, 0)  # Preto
        white = QColor(255, 255, 255)  # Branco

        # Desenhar um triângulo superior amarelo
        painter.setBrush(yellow)
        polygon_yellow = [
            QPoint(0, 0),
            QPoint(self.width(), 0),
            QPoint(self.width(), self.height()),
        ]
        painter.drawPolygon(polygon_yellow)

        # Desenhar um triângulo inferior preto
        painter.setBrush(black)
        polygon_black = [
            QPoint(0, 0),
            QPoint(0, self.height()),
            QPoint(self.width(), self.height()),
        ]
        painter.drawPolygon(polygon_black)

        # Desenhar um quadrado branco no meio (preenchendo a parte interna)
        square_size = 200
        painter.setBrush(white)
        painter.drawRect(
            (self.width() - square_size) // 2,
            (self.height() - square_size) // 2,
            square_size,
            square_size,
        )

        # Carregar a imagem
        image_path = "simbolo ut.png"
        pixmap = QPixmap(image_path)

        # Desenhar a imagem dentro do quadrado branco
        painter.drawPixmap(
            (self.width() - square_size) // 2,
            (self.height() - square_size) // 2,
            square_size,
            square_size,
            pixmap.scaled(square_size, square_size, Qt.KeepAspectRatio),
        )
