from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class cardapioTela(QMainWindow):
    def __init__(self, cor_amarelo=(255, 218, 185), cor_fundo=(200, 200, 200), cor_cinza=(169, 169, 169), proporcao_amarelo=1, proporcao_cinza=3):
        super().__init__()

        self.setWindowTitle("Nova Tela")
        self.setGeometry(200, 200, 600, 400)

        # Criar um widget para a nova tela
        widget = QWidget(self)

        # Configurar o layout como uma caixa vertical
        layout = QVBoxLayout(widget)

        # Criar uma etiqueta para a parte amarela (20%)
        parte_amarela = QLabel()
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
            layout_quadrados_cinza.addWidget(quadrado_cinza)

        # Adicionar a parte cinza ao layout principal
        layout.addWidget(parte_cinza, proporcao_cinza)

        # Definir o layout principal do widget
        widget.setLayout(layout)

        # Definir o widget como o widget central da janela
        self.setCentralWidget(widget)

