import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QSize

class SaldoWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Saldo")
        self.setGeometry(100, 100, 600, 400)

        # Criar um widget personalizado
        custom_widget = SaldoWidget(self)
        self.setCentralWidget(custom_widget)

class SaldoWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Configurar o layout como uma caixa vertical
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        layout.setSpacing(20)  # Definir espaçamento entre os widgets

        # Criar uma etiqueta para a mensagem "Saldo"
        self.label_saldo = QLabel("Meu Saldo")
        self.label_saldo.setAlignment(Qt.AlignCenter)
        self.label_saldo.setStyleSheet("font-size: 40px; font-family: italic;")  # Definir tamanho e família da fonte

        # Criar uma etiqueta para o valor (substitua '1000.00' pelo valor real)
        self.label_valor = QLabel("R$ xxxxx")
        self.label_valor.setAlignment(Qt.AlignCenter)
        self.label_valor.setStyleSheet("font-size: 30px; font-family: italic;")  # Definir tamanho e família da fonte

        # Adicionar as etiquetas ao layout
        layout.addWidget(self.label_saldo)
        layout.addWidget(self.label_valor)

        # Adicionar um espaço vertical entre as etiquetas e os retângulos
        layout.addSpacing(40)  # Aumentar o espaçamento

        # Adicionar dois retângulos roxos arredondados e dimensionados como quadrados perfeitos
        self.retangulo1 = QLabel("Pix")
        self.retangulo1.setStyleSheet("background-color: #bb8fce; color: white; border-radius: 15px; font-size: 20px;")  # Ajuste o tamanho da fonte aqui
        self.retangulo1.setAlignment(Qt.AlignCenter)

        self.retangulo2 = QLabel("Cartão de Crédito / \nDébito ")
        self.retangulo2.setStyleSheet("background-color: #bb8fce; color: white; border-radius: 15px; font-size: 20px;")
        self.retangulo2.setAlignment(Qt.AlignCenter)

        # Ajustar a largura dos retângulos
        retangulo_width = max(350, int(self.height() / 6))
        retangulo_height = max(150, int(self.height() / 6))
        self.retangulo1.setMinimumSize(retangulo_width, retangulo_height)
        self.retangulo2.setMinimumSize(retangulo_width, retangulo_height)

        # Adicionar os retângulos ao layout
        layout.addWidget(self.retangulo1)
        layout.addWidget(self.retangulo2)

        # Configurar o layout principal do widget
        self.setLayout(layout)

        # Chamar a função para ajustar tamanhos
        self.updateSizes()

        # Adicionar o botão de voltar
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

    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")

    def resizeEvent(self, event):
        # Redefinir os tamanhos proporcionais quando a janela for redimensionada
        self.updateSizes()

    def updateSizes(self):
        # Obter a altura atual da janela
        height = self.height()

        # Ajustar o tamanho da fonte proporcionalmente à altura da janela
        font_size_saldo = max(14, int(height / 20))
        font_size_valor = max(12, int(height / 25))
        font_size_mensagem = max(12, int(height / 25))

        # Atualizar os tamanhos das fontes
        self.label_saldo.setFont(QFont("italic", font_size_saldo))
        self.label_valor.setFont(QFont("italic", font_size_valor))

        # Ajustar o tamanho dos retângulos proporcionalmente à altura da janela
        retangulo_width = max(200, int(height / 6))
        retangulo_height = max(60, int(height / 6))

        # Atualizar os tamanhos dos retângulos
        self.retangulo1.setMinimumSize(retangulo_width, retangulo_height)
        self.retangulo2.setMinimumSize(retangulo_width, retangulo_height)

if __name__ == "__main__":
    app = QApplication([])

    window = SaldoWindow()
    window.show()

    app.exec_()
