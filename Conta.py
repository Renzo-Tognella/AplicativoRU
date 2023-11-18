import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, QImage, QPainter, QColor
from PySide6.QtCore import Qt
import barcode
from barcode.writer import ImageWriter

class ContaApp(QWidget):
    def __init__(self,cor_fundo=(248, 237, 237)):
        super(ContaApp, self).__init__()

        self.setWindowTitle("Tela de Conta")

        # Criar um layout vertical
        layout = QVBoxLayout(self)

        # Adicionar a imagem do brasao da reoublica brasileira
        imagem_path = "caminho/para/sua/imagem.png"  # Substitua pelo caminho onde esta salva a imagem
        imagem_label = QLabel(self)
        pixmap = QPixmap(imagem_path)
        imagem_label.setPixmap(pixmap.scaledToWidth(600, Qt.SmoothTransformation)) #verificar se o tamanho ta certo
        layout.addWidget(imagem_label)
        
        # Adicionar o texto "Ministério da Educação" abaixo da imagem
        texto_label = QLabel("Ministério da Educação\n Universidade Tecnológica Federal do Paraná", self)
        texto_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(texto_label)

        # Adicionar um botão para escolher uma imagem
        self.botao_imagem = QPushButton("Escolher Imagem")
        self.botao_imagem.clicked.connect(self.escolher_imagem)
        layout.addWidget(self.botao_imagem)

        # Adicionar campos de texto para nome do usuário, campus e departamento
        self.nome_usuario = QLineEdit(self)
        self.nome_usuario.setPlaceholderText("Nome do Usuário")
        layout.addWidget(self.nome_usuario)

        self.campus = QLineEdit(self)
        self.campus.setPlaceholderText("Campus")
        layout.addWidget(self.campus)

        self.departamento = QLineEdit(self)
        self.departamento.setPlaceholderText("Departamento")
        layout.addWidget(self.departamento)

        # Adicionar um QLabel para exibir a imagem escolhida
        self.imagem_label = QLabel(self)
        layout.addWidget(self.imagem_label)

        # Adicionar um QLabel para exibir o código de barras
        self.codigo_barras_label = QLabel(self)
        layout.addWidget(self.codigo_barras_label)

        # Adicionar um botão para gerar o código de barras
        self.botao_codigo_barras = QPushButton("Gerar Código de Barras")
        self.botao_codigo_barras.clicked.connect(self.gerar_codigo_barras)
        layout.addWidget(self.botao_codigo_barras)

        # Configurar o layout do widget principal
        self.setLayout(layout)

    def escolher_imagem(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        arquivo, _ = QFileDialog.getOpenFileName(self, "Escolher Imagem", "", "Imagens (*.png *.jpg *.bmp *.gif *.tif *.tiff);;Todos os Arquivos (*)", options=options)

        if arquivo:
            pixmap = QPixmap(arquivo)
            self.imagem_label.setPixmap(pixmap.scaledToWidth(150, Qt.SmoothTransformation))

    def gerar_codigo_barras(self):
        nome_usuario = self.nome_usuario.text()
        campus = self.campus.text()
        departamento = self.departamento.text()
        registro_academico = "1234567"  # Substitua pelo registro acadêmico real

        # Concatenar as informações para gerar o código de barras
        dados_codigo_barras = f"{nome_usuario} - {campus} - {departamento} - {registro_academico}"

        # Gerar o código de barras como um arquivo PNG
        codigo_barras = barcode.Code128(dados_codigo_barras, writer=ImageWriter())
        arquivo_codigo_barras = codigo_barras.save('codigo_barras')

        # Exibir o código de barras na interface gráfica
        pixmap = QPixmap(arquivo_codigo_barras)
        self.codigo_barras_label.setPixmap(pixmap.scaledToWidth(200, Qt.SmoothTransformation))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContaApp()
    window.show()
    sys.exit(app.exec())
