from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtGui import QPainter, QColor, QFont, QPixmap
from PySide6.QtCore import Qt, QSize

class HistoricocomprasApp(QWidget):
    def __init__(self, cor_fundo=(248, 237, 237)):
        super().__init__()
        self.setWindowTitle("Histórico de Compras de Tickets")

        # Criar um layout vertical
        layout = QVBoxLayout(self)

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
        caixa1 = QFrame(self)
        caixa1.setFrameShape(QFrame.StyledPanel)
        caixa1.setStyleSheet("background-color: rgb(200, 200, 200);")  # Cor cinza

        # Adicionar informações à primeira caixa
        label1 = QLabel("Tipo de Refeição: Almoço\nData e Hora: 01/01/2023 12:30\nLocal: UTFPR Campus Curitiba - Centro", caixa1)
        font1 = QFont("Biome Light", 12)  
        label1.setFont(font1)
        layout.addWidget(caixa1)

        # Criar a segunda caixa de cor cinza
        caixa2 = QFrame(self)
        caixa2.setFrameShape(QFrame.StyledPanel)
        caixa2.setStyleSheet("background-color: rgb(200, 200, 200);")  # Cor cinza

        # Adicionar informações à segunda caixa
        label2 = QLabel("Tipo de Refeição: Jantar\nData e Hora: 05/02/2023 19:00\nLocal: UTFPR Campus Curitiba - Ecoville", caixa2)
        font2 = QFont("Biome Light", 12)  
        label2.setFont(font2)
        layout.addWidget(caixa2)

        # Configurar o layout do widget principal
        self.setLayout(layout)

    def voltar_pagina_anterior(self):
        print("Voltando à página anterior")

if __name__ == "__main__":
    app = QApplication([])
    window = HistoricocomprasApp()
    window.show()
    app.exec()
