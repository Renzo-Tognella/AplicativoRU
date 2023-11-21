import sys
<<<<<<< HEAD
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from PySide6.QtGui import QPixmap, QImage
=======
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QMainWindow
from PySide6.QtGui import QPixmap, QImage, QFont
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
from PySide6.QtCore import Qt, QSize
import barcode
from barcode.writer import ImageWriter
import tempfile
import os
from PIL import Image
import io


class ContaApp(QMainWindow):
    def __init__(self, cor_fundo=(248, 237, 237)):
        super(ContaApp, self).__init__()

        self.setWindowTitle("Tela de Conta")
        self.setGeometry(100, 100, 600, 400)

<<<<<<< HEAD
=======
        # Criar um widget para a nova tela
        widget = QWidget(self)

        # Configurar o layout como uma caixa vertical
        layout = QVBoxLayout(widget)

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

        # Adicionar o botão de voltar ao layout
        layout.addWidget(self.botao_voltar, alignment=Qt.AlignTop | Qt.AlignLeft)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f

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
<<<<<<< HEAD
=======
        self.nome_usuario.setText("Aluno: Renzo Nogarotto")
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
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


<<<<<<< HEAD
        self.setLayout(layout)

    def gerar_codigo_barras(self, nome, curso, ra):
        nome_usuario = nome.replace('ç', 'c').replace('ã', 'a') 
        departamento = curso.replace('ç', 'c').replace('ã', 'a')
        registro_academico = str(ra)  
=======
        # Configurar o layout do widget principal
        widget.setLayout(layout)

        # Definir o widget como o widget central da janela
        self.setCentralWidget(widget)

    def gerar_codigo_barras(self):
        nome_usuario = "Renzo Nogarotto"
        campus = "Curitiba"
        departamento = "BSI"
        registro_academico = "a2413949"  # Substitua pelo registro acadêmico real
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f

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

<<<<<<< HEAD
=======
    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContaApp()
    window.show()
    sys.exit(app.exec())
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
