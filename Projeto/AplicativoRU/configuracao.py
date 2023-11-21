import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout

class ProfileConfigWindow(QWidget):
    def __init__(self):
        super(ProfileConfigWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Configuração de Perfil')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)

        # Adicionar o botão de voltar no canto superior esquerdo
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

        # Adicionar os botões no meio da tela abaixo do botão de voltar
        # Botão Ajuda (azul)
        self.botao_ajuda = QPushButton('Ajuda', self)
        self.botao_ajuda.setObjectName("ajuda")
        self.botao_ajuda.setStyleSheet("background-color: blue; color: white;")
        self.botao_ajuda.clicked.connect(self.exibir_ajuda)

        # Botão Contato (verde)
        self.botao_contato = QPushButton('Contato', self)
        self.botao_contato.setObjectName("contato")
        self.botao_contato.setStyleSheet("background-color: green; color: white;")
        self.botao_contato.clicked.connect(self.exibir_contato)

        # Botão Sair (vermelho)
        self.botao_sair = QPushButton('Sair', self)
        self.botao_sair.setObjectName("sair")
        self.botao_sair.setStyleSheet("background-color: red; color: white;")
        self.botao_sair.clicked.connect(self.sair)

        button_layout = QVBoxLayout()

        button_layout.addWidget(self.botao_ajuda)  # Adicionar o botão Ajuda
        button_layout.addWidget(self.botao_contato)  # Adicionar o botão Contato
        button_layout.addWidget(self.botao_sair)  # Adicionar o botão Sair

        layout.addWidget(self.botao_voltar)  # Adicionar o botão de voltar
        layout.addLayout(button_layout)

    def voltar_pagina_anterior(self):
        # Adicione a lógica para voltar à página anterior aqui
        print("Voltar à página anterior")

    def sair(self):
        # Adicione a lógica para sair aqui
        print("Sair")

    def exibir_ajuda(self):
        # Adicione a lógica para exibir a ajuda aqui
        print("Exibir ajuda")

    def exibir_contato(self):
        # Adicione a lógica para exibir informações de contato aqui
        print("Exibir informações de contato")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileConfigWindow()
    window.show()
    sys.exit(app.exec_())
