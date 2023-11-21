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
<<<<<<< HEAD
        self.setGeometry(100, 100, 400, 300) 
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop) 

=======
        self.setGeometry(100, 100, 400, 300)  # Ajustado a altura da janela para acomodar o QLabel abaixo do botão

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)  # Alinhar o layout no topo

        # Adicionar o botão de voltar no canto superior esquerdo
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        self.botao_voltar = QPushButton(self)
        self.botao_voltar.setObjectName("voltar")
        self.botao_voltar.setIcon(QPixmap("Projeto/AplicativoRU/back.png"))
        self.botao_voltar.setIconSize(QSize(40, 40))
<<<<<<< HEAD
        layout.addWidget(self.botao_voltar, alignment=Qt.AlignLeft)
=======
        self.botao_voltar.clicked.connect(self.voltar_para)
        layout.addWidget(self.botao_voltar, alignment=Qt.AlignLeft)

        # Adicionar campo para inserir um valor
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        self.label_valor = QLabel('Insira o valor:', self)
        self.edit_valor = QLineEdit(self)
        self.edit_valor.setStyleSheet("padding: 5px; font-size: 14px;")
        self.label_valor.setStyleSheet("font-size: 16px; margin-bottom: 5px;")
<<<<<<< HEAD
        layout.addWidget(self.label_valor, alignment=Qt.AlignTop | Qt.AlignHCenter) 
        layout.addWidget(self.edit_valor, alignment=Qt.AlignTop | Qt.AlignHCenter)

=======
        layout.addWidget(self.label_valor, alignment=Qt.AlignTop | Qt.AlignHCenter)  # Alinhar ao topo e centralizar horizontalmente
        layout.addWidget(self.edit_valor, alignment=Qt.AlignTop | Qt.AlignHCenter)

        # Adicionar botão verde para comprar
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        self.botao_comprar = QPushButton('COMPRAR', self)
        self.botao_comprar.setObjectName("comprar")
        self.botao_comprar.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; font-size: 16px;")
        self.botao_comprar.clicked.connect(self.exibir_imagem_qrcode)
        layout.addWidget(self.botao_comprar, alignment=Qt.AlignTop | Qt.AlignHCenter)

<<<<<<< HEAD
        self.label_qrcode = QLabel(self)
        self.label_qrcode.hide()  
    def exibir_imagem_qrcode(self):
        tamanho_janela = QSize(self.width(), self.height())
        tamanho_qrcode = QSize(tamanho_janela.width() * 0.2, tamanho_janela.height() * 0.2) 
        self.label_qrcode.setPixmap(QPixmap("Projeto/AplicativoRU/qrcode.png").scaled(tamanho_qrcode, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
=======
        # QLabel para exibir a imagem "qrcode.png" abaixo do botão COMPRAR
        self.label_qrcode = QLabel(self)
        self.label_qrcode.hide()  # Inicialmente, a imagem está oculta

    def voltar_para(self):
        self.close()

    def exibir_imagem_qrcode(self):
        # Adicionar dinamicamente a imagem "qrcode.png" abaixo do botão COMPRAR
        tamanho_janela = QSize(self.width(), self.height())
        tamanho_qrcode = QSize(tamanho_janela.width() * 0.2, tamanho_janela.height() * 0.2)  # Porcentagem ajustável
        self.label_qrcode.setPixmap(QPixmap("Projeto/AplicativoRU/qrcode.png").scaled(tamanho_qrcode, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        
        # Ajustar a geometria para centralizar com o botão COMPRAR
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        x_qrcode = (tamanho_janela.width() - tamanho_qrcode.width()) / 1.81
        y_qrcode = self.botao_comprar.y() + self.botao_comprar.height() + 20
        self.label_qrcode.setGeometry(x_qrcode, y_qrcode, tamanho_qrcode.width(), tamanho_qrcode.height())
        self.label_qrcode.show()

    def gerar_qr_code(self):
        valor = self.edit_valor.text()
        if valor:
            print(f"Gere o QR Code para o valor: {valor}")
<<<<<<< HEAD

=======
            # Lógica para gerar o QR Code aqui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pix_page = PixPage()
    pix_page.show()
    sys.exit(app.exec_())
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
