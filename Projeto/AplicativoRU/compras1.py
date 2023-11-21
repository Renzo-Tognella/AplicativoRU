import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout

class ProfileConfigWindow(QWidget):
    def __init__(self):
        super(ProfileConfigWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Configuração de Perfil')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)

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

        button_layout = QHBoxLayout()

        # Adicionando botões de atualização
        update_name_button = QPushButton('Atualizar Nome', self)
        update_name_button.clicked.connect(self.update_name)

        update_email_button = QPushButton('Atualizar E-mail', self)
        update_email_button.clicked.connect(self.update_email)

        button_layout.addWidget(self.botao_voltar)  # Adicionar o botão de voltar
        button_layout.addWidget(update_name_button)
        button_layout.addWidget(update_email_button)

        layout.addLayout(button_layout)

        form_layout = QFormLayout()

        self.name_edit = QLineEdit(self)
        self.email_edit = QLineEdit(self)

        form_layout.addRow('Nome:', self.name_edit)
        form_layout.addRow('E-mail:', self.email_edit)

        layout.addLayout(form_layout)

    def update_name(self):
        # Aqui você pode adicionar lógica para atualizar o nome
        print("Nome atualizado!")

    def update_email(self):
        # Aqui você pode adicionar lógica para atualizar o e-mail
        print("E-mail atualizado!")

    def voltar_pagina_anterior(self):
        # Adicione a lógica para voltar à página anterior aqui
        print("Voltar à página anterior")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileConfigWindow()
    window.show()
    sys.exit(app.exec_())
