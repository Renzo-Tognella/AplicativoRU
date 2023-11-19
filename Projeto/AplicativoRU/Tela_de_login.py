from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QFrame, QGridLayout
from PySide6.QtGui import QFont  # Importe a classe QFont do módulo QtGui

class telaDeLogin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")

        layout = QVBoxLayout()
        self.label_ra = QLabel("RA")
        self.text_ra = QLineEdit()
        self.text_ra.setFixedWidth(200)
        self.text_ra.setStyleSheet('background-color: lightgrey; border-radius: 30px; border: 2px solid lightgrey; padding: 5px;')
        layout.addWidget(self.label_ra)
        layout.addWidget(self.text_ra)

        self.label_senha = QLabel("Senha")
        self.text_senha = QLineEdit()
        self.text_senha.setEchoMode(QLineEdit.Password)
        self.text_senha.setFixedWidth(200)
        self.text_senha.setStyleSheet('background-color: lightgrey; border-radius: 30px; border: 2px solid lightgrey; padding: 5px;')
        layout.addWidget(self.label_senha)
        layout.addWidget(self.text_senha)

        self.button = QPushButton("Entrar")
        self.button.setFixedWidth(200)
        self.button.setStyleSheet('background-color: #D9B7F4; border-radius: 40px; padding: 10px;')
        layout.addWidget(self.button)

        self.hint = QLabel("Dica: Use a seu registro acadêmico e \na senha do Portal do Aluno")
        self.hint.setFixedWidth(200)
        self.hint.setMinimumHeight(50)
        layout.addWidget(self.hint)

        # Criar uma fonte personalizada usando QFont do módulo QtGui
        font = QFont()
        font2 = QFont()
        font.setPointSize(9)  # Defina o tamanho da fonte
        font.setFamily("italic")  # Defina a família da fonte
        font.setBold(False)  # Defina como negrito
        font2.setBold(True)


        # Aplicar a fonte aos widgets relevantes
        self.label_ra.setFont(font)
        self.text_ra.setFont(font)
        self.label_senha.setFont(font)
        self.text_senha.setFont(font)
        self.button.setFont(font2)
        self.hint.setFont(font)

        # Criar um frame para o formulário
        frame = QFrame()
        frame.setLayout(layout)
        frame.setStyleSheet("background-color: #FFF059; border-radius: 20px;")

        # Criar um layout para a janela
        window_layout = QGridLayout()
        window_layout.setRowStretch(0, 1)
        window_layout.setRowStretch(2, 1)
        window_layout.setColumnStretch(0, 1)
        window_layout.setColumnStretch(2, 1)
        window_layout.addWidget(frame, 1, 1)
        container = QWidget()
        container.setLayout(window_layout)
        self.setCentralWidget(container)

        # Definir a cor de fundo
        self.setStyleSheet("background-color: #F8EDED;")


