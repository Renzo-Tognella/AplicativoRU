from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtGui import QColor, QFont, QPixmap
from PySide6.QtCore import Qt, QSize

class VerticalLine(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(2)
        self.setStyleSheet("color: black;")

class FloatingSquares(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Definir a cor dos quadrados como cinza claro
        cor_cinza_claro = QColor(200, 200, 200)

        # Adicionar um botão de voltar no canto superior esquerdo
        x_voltar = 10
        y_voltar = 10
        square_size_voltar = 40

        self.botao_voltar = QPushButton(self)
        self.botao_voltar.setObjectName("voltar")
        self.botao_voltar.setFixedSize(square_size_voltar, square_size_voltar)
        self.botao_voltar.move(x_voltar, y_voltar)
        image_path_inside_square_voltar = "Projeto/AplicativoRU/back.png"
        self.botao_voltar.setIcon(QPixmap(image_path_inside_square_voltar))
        tamanho_icone_voltar = QSize(70, 70)
        self.botao_voltar.setIconSize(tamanho_icone_voltar)
        self.botao_voltar.clicked.connect(self.voltar_pagina_anterior)

        # Adicionar uma mensagem acima dos quadrados
        self.message_label = QLabel("Histórico de Tickets", self)
        self.message_label.setAlignment(Qt.AlignCenter)

        # Configurar a fonte e o tamanho da mensagem
        fonte_mensagem = QFont()
        fonte_mensagem.setPointSize(16)
        fonte_mensagem.setBold(False)
        fonte_mensagem.setItalic(True)
        self.message_label.setFont(fonte_mensagem)

        # Criar dois widgets para representar os quadrados
        self.square1 = QLabel("Refeição Tipo\n\nDD/MM/AA       HH:MM\n\nUTFPR Campus Curitiba", self)
        self.square2 = QLabel("Refeição Tipo\n\nDD/MM/AA       HH:MM\n\nUTFPR Campus Curitiba", self)

        # Configurar a cor dos quadrados e aumentar a área
        self.square1.setStyleSheet(f"background-color: {cor_cinza_claro.name()}; border-radius: 20px;")
        self.square2.setStyleSheet(f"background-color: {cor_cinza_claro.name()}; border-radius: 20px;")

        # Configurar o texto na caixa
        self.square1.setAlignment(Qt.AlignCenter)
        self.square2.setAlignment(Qt.AlignCenter)

        # Configurar a fonte e o tamanho do texto nas caixas cinzas (itálico)
        fonte_caixas_cinzas_italico = QFont()
        fonte_caixas_cinzas_italico.setPointSize(14)
        fonte_caixas_cinzas_italico.setItalic(True)

        self.square1.setFont(fonte_caixas_cinzas_italico)
        self.square2.setFont(fonte_caixas_cinzas_italico)

        # Criar uma linha vertical preta
        linha_vertical = VerticalLine(self)

        # Layout vertical para posicionar a mensagem, a linha e os quadrados
        layout = QVBoxLayout(self)
        layout.addWidget(self.botao_voltar, 0, Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.message_label, 0, Qt.AlignCenter)
        layout.addSpacing(40)  # Aumentar o espaçamento entre a mensagem e as caixas
        layout.addWidget(linha_vertical, 0, Qt.AlignCenter)
        layout.addSpacing(60)  # Aumentar o espaçamento entre as caixas cinzas
        layout.addWidget(self.square1, 0, Qt.AlignCenter)
        layout.addWidget(self.square2, 0, Qt.AlignCenter)

        self.setLayout(layout)

    def resizeEvent(self, event):
        # Redefinir o tamanho dos quadrados ao redimensionar a tela
        tamanho_quadrado = 250  # Tamanho fixo dos quadrados
        self.square1.setFixedSize(tamanho_quadrado, tamanho_quadrado)
        self.square2.setFixedSize(tamanho_quadrado, tamanho_quadrado)

    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")

class MinhaTela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha Tela")

        # Criar um widget para a nova tela
        widget = QWidget(self)

        # Configurar o layout como uma caixa vertical
        layout = QVBoxLayout(widget)

        # Adicionar o widget com os quadrados flutuantes ao layout
        floating_squares = FloatingSquares(widget)
        layout.addWidget(floating_squares, 0, Qt.AlignCenter)

        # Configurar o layout principal do widget
        widget.setLayout(layout)

        # Definir o widget como o widget central da janela
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])

    minha_tela = MinhaTela()
    minha_tela.show()

    app.exec_()
