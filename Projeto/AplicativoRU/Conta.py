import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QSize
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
        layout.addWidget(self.botao_voltar)

        imagem_path = "Projeto/AplicativoRU/brasaooficialcolorido.png"  
        imagem_label = QLabel(self)
        pixmap = QPixmap(imagem_path)
        imagem_label.setPixmap(pixmap.scaledToWidth(600, Qt.SmoothTransformation)) 
        layout.addWidget(imagem_label)
        imagem_label.setAlignment(Qt.AlignCenter)

   
        texto_label = QLabel("Ministério da Educação\nUniversidade Tecnológica Federal do Paraná", self)
        texto_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(texto_label)

        self.botao_imagem = QPushButton("Escolher Imagem")
        self.botao_imagem.clicked.connect(self.escolher_imagem)
        layout.addWidget(self.botao_imagem)

        self.nome_usuario = QLabel(self)
        self.nome_usuario.setAlignment(Qt.AlignCenter)
        self.nome_usuario.setStyleSheet('font-size: 24px')
        layout.addWidget(self.nome_usuario)

        self.departamento = QLabel(self)
        self.departamento.setStyleSheet('font-size: 24px')
        self.departamento.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.departamento)

        self.ra = QLabel(self)
        self.ra.setStyleSheet('font-size: 24px')
        self.ra.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.ra)

        self.imagem_label = QLabel(self)
        layout.addWidget(self.imagem_label)

        self.codigo_barras_label = QLabel(self)
        layout.addWidget(self.codigo_barras_label)


        self.setLayout(layout)

    def gerar_codigo_barras(self, nome, curso, ra):
        nome_usuario = nome.replace('ç', 'c').replace('ã', 'a') 
        departamento = curso.replace('ç', 'c').replace('ã', 'a')
        registro_academico = str(ra)  

        dados_codigo_barras = f"{nome_usuario} - {departamento} - {ra} - {registro_academico}"

        codigo_barras = barcode.Code128(dados_codigo_barras, writer=ImageWriter())
        arquivo_codigo_barras = codigo_barras.save('codigo_barras')

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

