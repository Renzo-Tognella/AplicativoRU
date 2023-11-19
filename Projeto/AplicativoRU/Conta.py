import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
import barcode
from barcode.writer import ImageWriter
import tempfile
import os
from PIL import Image
import io

class ContaApp(QWidget):
    def __init__(self, cor_fundo=(248, 237, 237)):
        super(ContaApp, self).__init__()

        self.setWindowTitle("Tela de Conta")

        # Criar um layout vertical
        layout = QVBoxLayout(self)

        

        # Adicionar a imagem do brasão da república brasileira
        imagem_path = "AplicativoRU/brasaooficialcolorido.png"  # Substitua pelo caminho onde esta salva a imagem
        imagem_label = QLabel(self)
        pixmap = QPixmap(imagem_path)
        imagem_label.setPixmap(pixmap.scaledToWidth(600, Qt.SmoothTransformation))  # verificar se o tamanho está certo
        layout.addWidget(imagem_label)
        imagem_label.setAlignment(Qt.AlignCenter)

        # Adicionar o texto "Ministério da Educação" abaixo da imagem
        texto_label = QLabel("Ministério da Educação\nUniversidade Tecnológica Federal do Paraná", self)
        texto_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(texto_label)

        # Adicionar um botão para escolher uma imagem
        self.botao_imagem = QPushButton("Escolher Imagem")
        self.botao_imagem.clicked.connect(self.escolher_imagem)
        layout.addWidget(self.botao_imagem)

        # Adicionar campos de texto para nome do usuário, campus e departamento
        self.nome_usuario = QLabel(self)
        self.nome_usuario.setText("Aluno: Renzo Tognella De Rosa")
        self.nome_usuario.setAlignment(Qt.AlignCenter)
        self.nome_usuario.setStyleSheet('font-size: 24px')
        layout.addWidget(self.nome_usuario)

        self.campus = QLabel(self)
        self.campus.setText("Campus: Curitiba")
        self.campus.setAlignment(Qt.AlignCenter)
        self.campus.setStyleSheet('font-size: 24px')
        layout.addWidget(self.campus)

        self.departamento = QLabel(self)
        self.departamento.setText("Curso: Sistemas Da Informação")
        self.departamento.setStyleSheet('font-size: 24px')
        self.departamento.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.departamento)

        # Adicionar um QLabel para exibir a imagem escolhida
        self.imagem_label = QLabel(self)
        layout.addWidget(self.imagem_label)

        self.codigo_barras_label = QLabel(self)
        self.gerar_codigo_barras()
        layout.addWidget(self.codigo_barras_label)

        # Gerar e exibir o código de barras

        # Configurar o layout do widget principal
        self.setLayout(layout)

    def gerar_codigo_barras(self):
        nome_usuario = "Renzo Tognella De Rosa"
        campus = "Curitiba"
        departamento = "BSI"
        registro_academico = "a2413949"  # Substitua pelo registro acadêmico real

        # Concatenar as informações para gerar o código de barras
        dados_codigo_barras = f"{nome_usuario} - {campus} - {departamento} - {registro_academico}"

        dados_codigo_barras = f"{nome_usuario} - {campus} - {departamento} - {registro_academico}"

        # Gerar o código de barras como um arquivo PNG
        codigo_barras = barcode.Code128(dados_codigo_barras, writer=ImageWriter())
        arquivo_codigo_barras = codigo_barras.save('codigo_barras')

        # Exibir o código de barras na interface gráfica
        pixmap = QPixmap(arquivo_codigo_barras)
        self.codigo_barras_label.setPixmap(pixmap.scaledToWidth(400, Qt.SmoothTransformation))
        self.codigo_barras_label.setAlignment(Qt.AlignCenter)
    def escolher_imagem(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        arquivo, _ = QFileDialog.getOpenFileName(self, "Escolher Imagem", "", "Imagens (*.png *.jpg *.bmp *.gif *.tif *.tiff);;Todos os Arquivos (*)", options=options)

        if arquivo:
            pixmap = QPixmap(arquivo)
            self.imagem_label.setPixmap(pixmap.scaledToWidth(250, Qt.SmoothTransformation))
            self.imagem_label.setAlignment(Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContaApp()
    window.show()
    sys.exit(app.exec())
