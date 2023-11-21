<<<<<<< HEAD
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QLineEdit, QPushButton
from PySide6.QtGui import QFont, QPixmap
=======
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtGui import QPainter, QColor, QFont, QPixmap
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
from PySide6.QtCore import Qt, QSize

class HistoricocomprasApp(QWidget):
    def __init__(self, cor_fundo=(248, 237, 237)):
        super().__init__()
        self.setWindowTitle("Histórico de Compras de Tickets")

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
        caixa = QFrame(self)
        caixa.setFrameShape(QFrame.StyledPanel)
        caixa.setStyleSheet("background-color: #FFF982;")

        font1 = QFont("Biome Light", 18)  
        inner_layout = QVBoxLayout(caixa)
        self.textT = QLabel("Bote o dia e o ano: Ano-Mes-Dia", caixa)
        self.textT.setFont(font1)
        self.buttonConfirmar = QPushButton("Confirmar")
        self.buttonConfirmar.setStyleSheet('background-color: lightgrey;border-radius: 5px;')
        self.buttonConfirmar.setFixedWidth(250)
        self.buttonConfirmar.setFixedHeight(30)
        self.text = QLineEdit(caixa)
        self.text.setFixedWidth(250)     
        self.text.setFixedHeight(30)   
        self.text.setStyleSheet('background-color: lightgrey; border-radius: 30px; border: 2px solid lightgrey; padding: 5px;')
        self.textT.setStyleSheet('background-color: rgb(222,221,12); border-radius: 30px; border: 2px solid rgb(222,221,12); padding: 5px;')
        self.textT.setAlignment(Qt.AlignCenter)
        self.text.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(self.textT, alignment=Qt.AlignCenter)
        inner_layout.addWidget(self.text, alignment=Qt.AlignCenter)
        inner_layout.addWidget(self.buttonConfirmar, alignment=Qt.AlignCenter)

        layout.addWidget(caixa)

        def criar_sub_caixa(pai):
            sub_caixa = QFrame(pai)
            sub_caixa.setFixedHeight(60)  
            sub_caixa.setStyleSheet("background-color:  rgb(222,221,12); border-radius: 5px;") 
            return sub_caixa

<<<<<<< HEAD
=======
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

        # Criar a primeira caixa de cor cinza
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        caixa1 = QFrame(self)
        caixa1.setFrameShape(QFrame.StyledPanel)
        caixa1.setStyleSheet("background-color: #FFF982;") 

        sub_caixa1 = criar_sub_caixa(caixa1)
        inner_layout1 = QVBoxLayout(caixa1)
        inner_layout1.addWidget(sub_caixa1)
        self.label1 = QLabel(caixa1)
        self.label1.setAlignment(Qt.AlignCenter)
        inner_layout1.addWidget(self.label1)
        self.label1.setFont(font1)
        
        layout.addWidget(caixa1)

        caixa2 = QFrame(self)
        caixa2.setFrameShape(QFrame.StyledPanel)
<<<<<<< HEAD
        caixa2.setStyleSheet("background-color: #FFF982;") 

        sub_caixa2 = criar_sub_caixa(caixa2)
        inner_layout2 = QVBoxLayout(caixa2)
        inner_layout2.addWidget(sub_caixa2)
        self.label2 = QLabel(caixa2)
        self.label2.setAlignment(Qt.AlignCenter)
        inner_layout2.addWidget(self.label2)
        font2 = QFont("Biome Light", 18)  
        self.label2.setFont(font2)
        
=======
        caixa2.setStyleSheet("background-color: rgb(200, 200, 200);")  # Cor cinza

        # Adicionar informações à segunda caixa
        label2 = QLabel("Tipo de Refeição: Jantar\nData e Hora: 05/02/2023 19:00\nLocal: UTFPR Campus Curitiba - Ecoville", caixa2)
        font2 = QFont("Biome Light", 12)  
        label2.setFont(font2)
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
        layout.addWidget(caixa2)

        self.setLayout(layout)
<<<<<<< HEAD
=======

    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")

if __name__ == "__main__":
    app = QApplication([])
    window = HistoricocomprasApp()
    window.show()
    app.exec()
>>>>>>> 17748713ce05f7bb9c5546e16e590d5266c2db7f
