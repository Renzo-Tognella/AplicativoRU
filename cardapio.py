from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

class NovaTela(QMainWindow):
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
        parte_amarela.setStyleSheet(f"background-color: {cor_amarela.name()};")  # Amarelo

        # Adicionar um layout horizontal para a parte amarela
        layout_amarela = QHBoxLayout(parte_amarela)

        # Adicionar um QLabel para o texto "Almoço" dentro da parte amarela
        label_amarelo_almoco = QLabel("Almoço")
        label_amarelo_almoco.setAlignment(Qt.AlignCenter)
        label_amarelo_almoco.setStyleSheet("color: black; font-size: 24px;")  # Cor e tamanho da fonte na parte amarela

        # Adicionar um QLabel para o texto "Jantar" dentro da parte amarela
        label_amarelo_jantar = QLabel("Jantar")
        label_amarelo_jantar.setAlignment(Qt.AlignCenter)
        label_amarelo_jantar.setStyleSheet("color: black; font-size: 24px;")  # Cor e tamanho da fonte na parte amarela

        # Adicionar os labels na horizontal dentro do layout da parte amarela
        layout_amarela.addWidget(label_amarelo_almoco)
        layout_amarela.addWidget(label_amarelo_jantar)

        # Adicionar a parte amarela ao layout principal
        layout.addWidget(parte_amarela, proporcao_amarelo)  # 20% da altura

        # Adicionar uma QLabel para a parte cinza (60%)
        parte_cinza = QLabel()
        cor_cinza = QColor(*cor_cinza)
        layout.addWidget(parte_cinza, proporcao_cinza)  # 60% da altura
        parte_cinza.setStyleSheet(f"background-color: {cor_cinza.name()};")

        # Adicionar um layout horizontal para os quadrados cinzas
        layout_quadrados_cinza = QHBoxLayout(parte_cinza)

        # Adicionar 4 quadrados cinzas com texto
        for texto in ["Almoço - semana DD/MM - DD/MM\n\nDia da semana DD/MM\n\nEste é um exemplo de refeição\nArroz\nArroz integral\nFeijão carioca\n salada\n Frango grelhado", "Janta - semana DD/MM - DD/MM\n\nDia da semana DD/MM\n\nEste é um exemplo de refeição\nArroz\nArroz integral\nFeijão carioca\n salada\n Alcatra grelhada"]:
            quadrado_cinza = QLabel(texto)
            quadrado_cinza.setAlignment(Qt.AlignCenter)
            quadrado_cinza.setStyleSheet("background-color: rgb(200,200,200); font-size: 20px;")  # Ajuste o tamanho da fonte
            quadrado_cinza.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layout_quadrados_cinza.addWidget(quadrado_cinza)

        # Adicionar a parte cinza ao layout principal
        layout.addWidget(parte_cinza, proporcao_cinza)

        # Definir o layout principal do widget
        widget.setLayout(layout)

        # Definir o widget como o widget central da janela
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication([])

    # Exemplo com tons diferentes de amarelo, fundo e cinza
    nova_tela = NovaTela(cor_amarelo=(255, 249, 130), cor_fundo=(0, 0, 0), cor_cinza=(255, 255, 255))
    nova_tela.show()

    app.exec_()