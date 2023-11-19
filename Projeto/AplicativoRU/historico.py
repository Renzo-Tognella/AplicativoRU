from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame, QLabel
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import Qt

class HistoricocomprasApp(QWidget):
    def __init__(self, cor_fundo=(248, 237, 237)):
        super().__init__()
        self.setWindowTitle("Histórico de Compras de Tickets")

        # Criar um layout vertical
        layout = QVBoxLayout(self)

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

if __name__ == "__main__":
    app = QApplication([])
    window = HistoricocomprasApp()
    window.show()
    app.exec()