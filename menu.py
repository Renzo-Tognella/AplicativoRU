from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen
from PySide6.QtCore import Qt

class WhiteSquaresWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quadrados Brancos com Imagem na Parte Amarela")
        self.setGeometry(100, 100, 600, 400)

        # Criar um widget personalizado
        custom_widget = WhiteSquaresWidget(self)
        self.setCentralWidget(custom_widget)

class WhiteSquaresWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Carregar as imagens
        self.image_paths = [
            "historico.png",
            "minha conta.png",
            "cardapio.png",
            "compras.png",
        ]
        self.images = [QPixmap(path) for path in self.image_paths]

        # Carregar a imagem para a parte amarela
        self.yellow_image = QPixmap("path/to/yellow_image.png")  # Substitua pelo caminho real da sua imagem amarela

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Configurar cores
        white = QColor(249, 249, 249, 0)  # Branco com alpha (transparência) configurado para 0
        yellow = QColor(255, 249, 130)  # Amarelo

        # Desenhar a parte superior amarela com a imagem
        painter.setBrush(yellow)
        painter.drawRect(0, 0, self.width(), 0.2 * self.height())
        painter.drawPixmap(0, 0, self.width(), 0.2 * self.height(), self.yellow_image)

        # Desenhar um quadrado branco pequeno no canto superior esquerdo da parte amarela
        square_size_amarela = 40
        x_amarela = 10  # Ajuste a posição x conforme necessário
        y_amarela = 10  # Ajuste a posição y conforme necessário
        pen_amarela = QPen(white)  # Configurar a caneta com cor branca e alpha 0 para tornar as bordas transparentes
        painter.setPen(pen_amarela)
        painter.setBrush(white)
        painter.drawRect(x_amarela, y_amarela, square_size_amarela, square_size_amarela)

        # Adicionar uma imagem dentro do quadrado branco
        image_path_inside_square_amarela = "engrenagem.png"  # Substitua pelo caminho real da sua imagem
        image_inside_square_amarela = QPixmap(image_path_inside_square_amarela)
        painter.drawPixmap(x_amarela, y_amarela, square_size_amarela, square_size_amarela, image_inside_square_amarela)

        # Desenhar o restante da tela branca
        painter.setBrush(white)
        painter.drawRect(0, 0.2 * self.height(), self.width(), 0.8 * self.height())

        # Tamanho dos quadrados (ajustado para ser menor)
        square_size_branca = min(self.width() // 8, 0.6 * self.height() // 4)

        # Posições dos quadrados (ajustadas para ficarem mais próximas e centralizadas)
        square_positions = [
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
        ]

        # Desenhar quatro quadrados brancos na parte branca
        for (x, y, width, height), image in zip(square_positions, self.images):
            pen_branca = QPen(white)  # Configurar a caneta com cor branca e alpha 0 para tornar as bordas transparentes
            painter.setPen(pen_branca)
            painter.setBrush(white)
            painter.drawRect(x, y, width, height)
            painter.drawPixmap(x, y, width, height, image)

if __name__ == "__main__":
    app = QApplication([])

    window = WhiteSquaresWindow()
    window.show()

    app.exec_()
