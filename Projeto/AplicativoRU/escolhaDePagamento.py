from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class telaEscolhaPag(QMainWindow):
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
        self.label_saldo.setStyleSheet("font-size: 40px; font-family: italic; font-weight: normal;")  # Remover negrito

        # Adicionar uma etiqueta para o valor (substitua '1000.00' pelo valor real)
        self.label_valor = QLabel("R$ xxxxx")
        self.label_valor.setAlignment(Qt.AlignCenter)
        self.label_valor.setStyleSheet("font-size: 30px; font-family: italic; font-weight: normal;")  # Remover negrito

        # Adicionar uma etiqueta para outra mensagem abaixo do valor
        self.label_mensagem_valor = QLabel("Como deseja pagar ?")
        self.label_mensagem_valor.setAlignment(Qt.AlignCenter)
        self.label_mensagem_valor.setStyleSheet("font-size: 32px; font-family: italic; font-weight: normal;")  # Remover negrito # Definir tamanho e família da fonte

        # Adicionar as etiquetas ao layout
        layout.addWidget(self.label_saldo)
        layout.addWidget(self.label_valor)
        layout.addWidget(self.label_mensagem_valor)

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
        self.label_mensagem_valor.setFont(QFont("italic", font_size_mensagem))

        # Ajustar o tamanho dos retângulos proporcionalmente à altura da janela
        retangulo_width = max(200, int(height / 6))
        retangulo_height = max(60, int(height / 6))

        # Atualizar os tamanhos dos retângulos
        self.retangulo1.setMinimumSize(retangulo_width, retangulo_height)
        self.retangulo2.setMinimumSize(retangulo_width, retangulo_height)
