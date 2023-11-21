import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

class Config(QWidget):
    def __init__(self):
        super(Config, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Configuração de Perfil')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)

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

        self.botao_ajuda = QPushButton('Ajuda', self)
        self.botao_ajuda.setObjectName("ajuda")
        self.botao_ajuda.setStyleSheet("background-color: blue; color: white;")

    
        self.botao_contato = QPushButton('Contato', self)
        self.botao_contato.setObjectName("contato")
        self.botao_contato.setStyleSheet("background-color: green; color: white;")

        self.botao_sair = QPushButton('Sair', self)
        self.botao_sair.setObjectName("sair")


        button_layout = QVBoxLayout()

        button_layout.addWidget(self.botao_ajuda)  
        button_layout.addWidget(self.botao_contato) 
        button_layout.addWidget(self.botao_sair)  

        layout.addWidget(self.botao_voltar)  
        layout.addLayout(button_layout)

