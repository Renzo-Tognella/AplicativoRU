from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSizePolicy, QGridLayout, QPushButton
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Qt, QSize

class cardapioTela(QMainWindow):
    def __init__(self, cor_amarelo=(255, 218, 185), cor_fundo=(200, 200, 200), cor_cinza=(169, 169, 169), proporcao_amarelo=1, proporcao_cinza=3):
        super().__init__()

        self.setWindowTitle("Nova Tela")
        self.setGeometry(200, 200, 600, 600)  

        self.widget = QWidget(self)

        self.layout = QVBoxLayout(self.widget)
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
        self.layout.addWidget(self.botao_voltar)
        self.parte_amarela = QLabel()
        cor_amarela = QColor(*cor_amarelo)
        self.parte_amarela.setStyleSheet(f"background-color: {cor_amarela.name()};")  
        self.layout_amarela = QVBoxLayout(self.parte_amarela)


        self.label_amarelo_almoco = QLabel("Almoço")
        self.label_amarelo_almoco.setAlignment(Qt.AlignCenter)
        self.label_amarelo_almoco.setStyleSheet("color: black; font-size: 24px;") 


        self.label_amarelo_jantar = QLabel("Jantar")
        self.label_amarelo_jantar.setAlignment(Qt.AlignCenter)
        self.label_amarelo_jantar.setStyleSheet("color: black; font-size: 24px;")  


        self.layout_amarela.addWidget(self.label_amarelo_almoco)
        self.layout_amarela.addWidget(self.label_amarelo_jantar)


        self.layout.addWidget(self.parte_amarela, proporcao_amarelo)  

 
        self.grid_layout_almoco = QGridLayout()
        self.labels_almoco = []

        for i, texto in enumerate(["Refeição 1", "Refeição 2", "Refeição 3", "Refeição 4", "Refeição 5", "Refeição 6"]):
            quadrado_cinza = QLabel(texto)
            quadrado_cinza.setAlignment(Qt.AlignCenter)
            quadrado_cinza.setStyleSheet("background-color: rgb(200,200,200); font-size: 20px;") 
            quadrado_cinza.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.grid_layout_almoco.addWidget(quadrado_cinza, i // 2, i % 2)
            self.labels_almoco.append(quadrado_cinza)


        self.parte_cinza_almoco = QWidget()
        self.parte_cinza_almoco.setStyleSheet(f"background-color: lightgrey;")
        self.parte_cinza_almoco.setLayout(self.grid_layout_almoco)
        self.layout.addWidget(self.parte_cinza_almoco, proporcao_cinza)  

        self.grid_layout_jantar = QGridLayout()
        self.labels_jantar = []

        for i, texto in enumerate(["Refeição 1", "Refeição 2", "Refeição 3", "Refeição 4", "Refeição 5", "Refeição 6"]):
            quadrado_cinza = QLabel(texto)
            quadrado_cinza.setAlignment(Qt.AlignCenter)
            quadrado_cinza.setStyleSheet("background-color: rgb(200,200,200); font-size: 20px;") 
            quadrado_cinza.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.grid_layout_jantar.addWidget(quadrado_cinza, i // 2, i % 2)
            self.labels_jantar.append(quadrado_cinza)

        self.parte_cinza_jantar = QWidget()
        self.parte_cinza_jantar.setStyleSheet(f"background-color: lightgrey;")
        self.parte_cinza_jantar.setLayout(self.grid_layout_jantar)
        self.layout.addWidget(self.parte_cinza_jantar, proporcao_cinza) 

        self.widget.setLayout(self.layout)


        self.setCentralWidget(self.widget)
