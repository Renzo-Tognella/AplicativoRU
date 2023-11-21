import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class PixPage(QWidget):
    def __init__(self, parent=None):
        super(PixPage, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Pagamento Pix')
        self.setGeometry(100, 100, 400, 300) 
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop) 

        self.botao_voltar = QPushButton(self)
        self.botao_voltar.setObjectName("voltar")
        self.botao_voltar.setIcon(QPixmap("Projeto/AplicativoRU/back.png"))
        self.botao_voltar.setIconSize(QSize(40, 40))
        layout.addWidget(self.botao_voltar, alignment=Qt.AlignLeft)
        self.label_valor = QLabel('Insira o valor:', self)
        self.edit_valor = QLineEdit(self)
        self.edit_valor.setStyleSheet("padding: 5px; font-size: 14px;")
        self.label_valor.setStyleSheet("font-size: 16px; margin-bottom: 5px;")
        layout.addWidget(self.label_valor, alignment=Qt.AlignTop | Qt.AlignHCenter) 
        layout.addWidget(self.edit_valor, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.botao_comprar = QPushButton('COMPRAR', self)
        self.botao_comprar.setObjectName("comprar")
        self.botao_comprar.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 16px;")
        self.botao_comprar.clicked.connect(self.exibir_imagem_qrcode)
        layout.addWidget(self.botao_comprar, alignment=Qt.AlignTop | Qt.AlignHCenter)

        self.label_qrcode = QLabel(self)
        self.label_qrcode.hide()  
    def exibir_imagem_qrcode(self):
        tamanho_janela = QSize(self.width(), self.height())
        tamanho_qrcode = QSize(tamanho_janela.width() * 0.2, tamanho_janela.height() * 0.2) 
        self.label_qrcode.setPixmap(QPixmap("Projeto/AplicativoRU/qrcode.png").scaled(tamanho_qrcode, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        x_qrcode = (tamanho_janela.width() - tamanho_qrcode.width()) / 1.81
        y_qrcode = self.botao_comprar.y() + self.botao_comprar.height() + 20
        self.label_qrcode.setGeometry(x_qrcode, y_qrcode, tamanho_qrcode.width(), tamanho_qrcode.height())
        self.label_qrcode.show()

    def gerar_qr_code(self):
        valor = self.edit_valor.text()
        if valor:
            print(f"Gere o QR Code para o valor: {valor}")

