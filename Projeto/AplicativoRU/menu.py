from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen
from PySide6.QtCore import Qt, QSize

class telaMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quadrados Brancos com Imagem na Parte Amarela")
        self.setGeometry(100, 100, 600, 400)

        custom_widget = WhiteSquaresWidget(self)
        self.setCentralWidget(custom_widget)
        self.yellow_image = QPixmap("path/to/yellow_image.png")

<<<<<<< HEAD
        x_amarela = 10  
        y_amarela = 10  
=======
        # Posições dos elementos
        x_amarela = 500  # Ajuste a posição x conforme necessário
        y_amarela = 10  # Ajuste a posição y conforme necessário
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        square_size_amarela = 40

        # Criar o botão
        self.buttonEngrenagem = QPushButton(self)
        self.buttonEngrenagem.setObjectName("engrenagem")  
        self.buttonEngrenagem.setFixedSize(square_size_amarela, square_size_amarela)
        self.buttonEngrenagem.move(x_amarela, y_amarela)
        image_path_inside_square_amarela = "Projeto/AplicativoRU/engrenagem.png"
        self.buttonEngrenagem.setIcon(QPixmap(image_path_inside_square_amarela))
        tamanho_icone_botao = QSize(41, 41)  
        self.buttonEngrenagem.setIconSize(tamanho_icone_botao)      

        
        self.buttonCompras = QPushButton(self)
        self.buttonCompras.setObjectName("compras")  
        self.buttonCompras.setFixedSize(150, 150)
<<<<<<< HEAD
        self.buttonCompras.move(1204, 680)
=======
        self.buttonCompras.move(1300, 580)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        image_path_inside_square_amarelaCompras = "Projeto/AplicativoRU/compras.png"
        self.buttonCompras.setIcon(QPixmap(image_path_inside_square_amarelaCompras))
        tamanho_icone_botaoCompras = QSize(151, 151)  
        self.buttonCompras.setIconSize(tamanho_icone_botaoCompras)      
        
        self.buttonConta = QPushButton(self)
        self.buttonConta.setObjectName("Conta")  
        self.buttonConta.setFixedSize(150, 150)
<<<<<<< HEAD
        self.buttonConta.move(1204, 250)
=======
        self.buttonConta.move(1300, 228)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        image_path_inside_square_amarelaConta = "Projeto/AplicativoRU/Conta.png"
        self.buttonConta.setIcon(QPixmap(image_path_inside_square_amarelaConta))
        tamanho_icone_botaoConta = QSize(151, 151)  
        self.buttonConta.setIconSize(tamanho_icone_botaoConta)      

        self.buttonHistorico = QPushButton(self)
        self.buttonHistorico.setObjectName("Conta") 
        self.buttonHistorico.setFixedSize(150, 150)
<<<<<<< HEAD
        self.buttonHistorico.move(565, 250)
=======
        self.buttonHistorico.move(200, 228)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        image_path_inside_square_amarelaHistorico = "Projeto/AplicativoRU/historico.png"
        self.buttonHistorico.setIcon(QPixmap(image_path_inside_square_amarelaHistorico))
        tamanho_icone_botaoHistorico = QSize(151, 151) 
        self.buttonHistorico.setIconSize(tamanho_icone_botaoHistorico)      

        self.buttonCardapio = QPushButton(self)
        self.buttonCardapio.setObjectName("Conta") 
        self.buttonCardapio.setFixedSize(150, 150)
<<<<<<< HEAD
        self.buttonCardapio.move(565, 680)
=======
        self.buttonCardapio.move(200, 580)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        image_path_inside_square_amarelaCardapio = "Projeto/AplicativoRU/cardapio.png"
        self.buttonCardapio.setIcon(QPixmap(image_path_inside_square_amarelaCardapio))
        tamanho_icone_botaoCardapio = QSize(151, 151)  
        self.buttonCardapio.setIconSize(tamanho_icone_botaoCardapio)      


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

    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")
        

class WhiteSquaresWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Carregar as imagens
        self.image_paths = [
            "AplicativoRU/historico.png",
            "AplicativoRU/minha conta.png",
            "AplicativoRU/cardapio.png",
            "AplicativoRU/compras.png",
        ]
        self.images = [QPixmap(path) for path in self.image_paths]
        self.yellow_image = QPixmap("path/to/yellow_image.png") 

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        
        white = QColor(249, 249, 249, 0)  
        yellow = QColor(255, 249, 130)  
        
        painter.setBrush(yellow)
        painter.drawRect(0, 0, self.width(), 0.2 * self.height())
        painter.drawPixmap(0, 0, self.width(), 0.2 * self.height(), self.yellow_image)

        square_size_amarela = 40
        x_amarela = 10 
        y_amarela = 10  
        pen_amarela = QPen(white) 
        painter.setPen(pen_amarela)
        painter.setBrush(white)
        painter.drawRect(x_amarela, y_amarela, square_size_amarela, square_size_amarela)

        painter.setBrush(white)
        painter.drawRect(0, 0.2 * self.height(), self.width(), 0.8 * self.height())

        square_size_branca = min(self.width() // 8, 0.6 * self.height() // 4)

        square_positions = [
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
        ]

        for (x, y, width, height), image in zip(square_positions, self.images):
            pen_branca = QPen(white)  
            painter.setPen(pen_branca)
            painter.setBrush(white)
            painter.drawRect(x, y, width, height)
            painter.drawPixmap(x, y, width, height, image)