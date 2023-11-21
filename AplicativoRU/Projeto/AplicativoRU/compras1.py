import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout

class compraCartao(QWidget):
    def __init__(self):
        super(compraCartao, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Pagamento por cartão')
        self.setGeometry(100, 100, 400, 300)  

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
        button_layout = QHBoxLayout()


        button_layout.addWidget(self.botao_voltar, Qt.AlignLeft)

        layout.addLayout(button_layout)

        form_layout = QFormLayout()

        self.name_edit = QLineEdit(self)
        self.email_edit = QLineEdit(self)

        self.card_number_edit = QLineEdit(self)
        self.expiry_date_edit = QLineEdit(self)
        self.cvv_edit = QLineEdit(self)

        form_layout.addRow('Nome:', self.name_edit)
        form_layout.addRow('E-mail:', self.email_edit)
        form_layout.addRow('Número do Cartão:', self.card_number_edit)
        form_layout.addRow('Data de Validade:', self.expiry_date_edit)
        form_layout.addRow('CVV:', self.cvv_edit)

        layout.addLayout(form_layout)

