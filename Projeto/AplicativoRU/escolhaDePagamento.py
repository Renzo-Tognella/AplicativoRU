<<<<<<< HEAD
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QSize
=======

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt, QSize

>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f

class telaEscolhaPag(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolha Pagamento")

<<<<<<< HEAD
=======
        # Criar um widget personalizado
        custom_widget = SaldoWidget(self)
        self.setCentralWidget(custom_widget)

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
        
        

class SaldoWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Configurar o layout como uma caixa vertical
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        layout = QVBoxLayout(self)
        

        central_widget = QWidget(self)
        central_layout = QVBoxLayout(central_widget)

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
        central_layout.addWidget(self.botao_voltar, alignment=Qt.AlignTop | Qt.AlignLeft)

        self.label_saldo = QLabel("Meu Saldo")
        self.label_saldo.setAlignment(Qt.AlignCenter)
        self.label_saldo.setStyleSheet("font-size: 40px; font-family: italic; font-weight: normal;")  # Remover negrito

        self.label_valor = QLabel()
        self.label_valor.setAlignment(Qt.AlignCenter)
        self.label_valor.setStyleSheet("font-size: 30px; font-family: italic; font-weight: normal;")  # Remover negrito

        self.label_mensagem_valor = QLabel("Como deseja pagar ?")
        self.label_mensagem_valor.setAlignment(Qt.AlignCenter)
        self.label_mensagem_valor.setStyleSheet("font-size: 32px; font-family: italic; font-weight: normal;")  # Remover negrito # Definir tamanho e família da fonte

        central_layout.addWidget(self.label_saldo)
        central_layout.addWidget(self.label_valor)
        central_layout.addWidget(self.label_mensagem_valor)


        central_layout.addSpacing(40) 

        self.botao_pix = QPushButton("Pix", self)
        self.botao_pix.setStyleSheet("background-color: #bb8fce; color: white; border-radius: 15px; font-size: 20px;")  # Ajuste o tamanho da fonte aqui

        self.botao_cartao = QPushButton("Cartão de Crédito / Débito", self)
        self.botao_cartao.setStyleSheet("background-color: #bb8fce; color: white; border-radius: 15px; font-size: 20px;")

        botao_width = max(350, int(self.height() / 6))
        botao_height = max(150, int(self.height() / 6))
        self.botao_pix.setFixedSize(botao_width, botao_height)
        self.botao_cartao.setFixedSize(botao_width, botao_height)

        central_layout.addWidget(self.botao_pix, alignment=Qt.AlignHCenter)
        central_layout.addWidget(self.botao_cartao, alignment=Qt.AlignHCenter)

        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        self.updateSizes()

    def resizeEvent(self, event):
        self.updateSizes()

    def updateSizes(self):
        height = self.height()

        font_size_saldo = max(14, int(height / 20))
        font_size_valor = max(12, int(height / 25))
        font_size_mensagem = max(12, int(height / 25))

        self.label_saldo.setFont(QFont("italic", font_size_saldo))
        self.label_valor.setFont(QFont("italic", font_size_valor))
        self.label_mensagem_valor.setFont(QFont("italic", font_size_mensagem))

        botao_width = max(200, int(height / 6))
        botao_height = max(60, int(height / 6))

        # Atualizar os tamanhos dos botões
        self.botao_pix.setFixedSize(botao_width, botao_height)
        self.botao_cartao.setFixedSize(botao_width, botao_height)
