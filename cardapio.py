from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QColor, QPainterPath, QPainter
from PySide6.QtCore import Qt

class RoundedWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)  # Ajuste o tamanho conforme necessário

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Criar um caminho para o retângulo arredondado
        path = QPainterPath()
        path.addRoundedRect(self.rect(), 10, 10)
        painter.fillPath(path, QColor(192, 192, 192))  # Cor cinza

class NovaTela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nova Tela")
        self.setGeometry(200, 200, 600, 400)

        # Criar um widget para a nova tela
        widget = QWidget(self)

        # Configurar o layout como uma caixa vertical
        layout = QVBoxLayout(widget)

        # Criar uma etiqueta para a parte amarela (20%)
        parte_amarela = QLabel()
        parte_amarela.setStyleSheet("background-color: #FFD700;")  # Amarelo
        layout.addWidget(parte_amarela, 1)  # 20% da altura

        # Criar uma etiqueta para a parte branca (60%)
        parte_branca = QLabel()
        layout.addWidget(parte_branca, 3)  # 60% da altura

        # Adicionar um retângulo arredondado cinza na parte branca
        retangulo_arredondado = RoundedWidget(parte_branca)
        retangulo_arredondado.setStyleSheet("background-color: transparent;")
        layout.addWidget(retangulo_arredondado, 1)  # 20% da altura

        # Configurar o layout principal do widget
        widget.setLayout(layout)

        # Definir o widget como o widget central da janela
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])

    nova_tela = NovaTela()
    nova_tela.show()

    app.exec_()
