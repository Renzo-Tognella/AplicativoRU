from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QPainter, QColor, QPixmap, QPen
from PySide6.QtCore import Qt, QSize

class telaMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quadrados Brancos com Imagem na Parte Amarela")
        self.setGeometry(100, 100, 600, 400)

        # Criar um widget personalizado
        custom_widget = WhiteSquaresWidget(self)
        self.setCentralWidget(custom_widget)
        self.yellow_image = QPixmap("path/to/yellow_image.png")  # Substitua pelo caminho real da sua imagem amarela

        # Posições dos elementos
        x_amarela = 10  # Ajuste a posição x conforme necessário
        y_amarela = 10  # Ajuste a posição y conforme necessário
        square_size_amarela = 40

        # Criar o botão
        self.buttonEngrenagem = QPushButton(self)
        self.buttonEngrenagem.setObjectName("engrenagem")  # Definir um nome para identificar o botão
        self.buttonEngrenagem.setFixedSize(square_size_amarela, square_size_amarela)
        self.buttonEngrenagem.move(x_amarela, y_amarela)
        image_path_inside_square_amarela = "Projeto/AplicativoRU/engrenagem.png"
        self.buttonEngrenagem.setIcon(QPixmap(image_path_inside_square_amarela))
        tamanho_icone_botao = QSize(41, 41)  # Substitua pelo tamanho desejado
        self.buttonEngrenagem.setIconSize(tamanho_icone_botao)      

        
        self.buttonCompras = QPushButton(self)
        self.buttonCompras.setObjectName("compras")  # Definir um nome para identificar o botão
        self.buttonCompras.setFixedSize(150, 150)
        self.buttonCompras.move(1845, 580)
        image_path_inside_square_amarelaCompras = "AplicativoRU/compras.png"
        self.buttonCompras.setIcon(QPixmap(image_path_inside_square_amarelaCompras))
        tamanho_icone_botaoCompras = QSize(151, 151)  # Substitua pelo tamanho desejado
        self.buttonCompras.setIconSize(tamanho_icone_botaoCompras)      
        
        self.buttonConta = QPushButton(self)
        self.buttonConta.setObjectName("Conta")  # Definir um nome para identificar o botão
        self.buttonConta.setFixedSize(150, 150)
        self.buttonConta.move(1845, 228)
        image_path_inside_square_amarelaConta = "AplicativoRU/Conta.png"
        self.buttonConta.setIcon(QPixmap(image_path_inside_square_amarelaConta))
        tamanho_icone_botaoConta = QSize(151, 151)  # Substitua pelo tamanho desejado
        self.buttonConta.setIconSize(tamanho_icone_botaoConta)      

        self.buttonHistorico = QPushButton(self)
        self.buttonHistorico.setObjectName("Conta")  # Definir um nome para identificar o botão
        self.buttonHistorico.setFixedSize(150, 150)
        self.buttonHistorico.move(565, 228)
        image_path_inside_square_amarelaHistorico = "AplicativoRU/historico.png"
        self.buttonHistorico.setIcon(QPixmap(image_path_inside_square_amarelaHistorico))
        tamanho_icone_botaoHistorico = QSize(151, 151)  # Substitua pelo tamanho desejado
        self.buttonHistorico.setIconSize(tamanho_icone_botaoHistorico)      

        self.buttonCardapio = QPushButton(self)
        self.buttonCardapio.setObjectName("Conta")  # Definir um nome para identificar o botão
        self.buttonCardapio.setFixedSize(150, 150)
        self.buttonCardapio.move(565, 580)
        image_path_inside_square_amarelaCardapio = "AplicativoRU/cardapio.png"
        self.buttonCardapio.setIcon(QPixmap(image_path_inside_square_amarelaCardapio))
        tamanho_icone_botaoCardapio = QSize(151, 151)  # Substitua pelo tamanho desejado
        self.buttonCardapio.setIconSize(tamanho_icone_botaoCardapio)      


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
        # Carregar a imagem para a parte amarela

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Configurar cores
        white = QColor(249, 249, 249, 0)  # Branco com alpha (transparência) configurado para 0
        yellow = QColor(255, 249, 130)  # Amarelo

        # Desenhar a parte superior amarela com a imagem
        painter.setBrush(yellow)
        painter.drawRect(0, 0, self.width(), 0.2 * self.height())
        painter.drawPixmap(0, 0, self.width(), 0.2 * self.height(), self.yellow_image)

        # Desenhar um quadrado branco pequeno no canto superior esquerdo da parte amarela
        square_size_amarela = 40
        x_amarela = 10  # Ajuste a posição x conforme necessário
        y_amarela = 10  # Ajuste a posição y conforme necessário
        pen_amarela = QPen(white)  # Configurar a caneta com cor branca e alpha 0 para tornar as bordas transparentes
        painter.setPen(pen_amarela)
        painter.setBrush(white)
        painter.drawRect(x_amarela, y_amarela, square_size_amarela, square_size_amarela)

        # Desenhar o restante da tela branca
        painter.setBrush(white)
        painter.drawRect(0, 0.2 * self.height(), self.width(), 0.8 * self.height())

        # Tamanho dos quadrados (ajustado para ser menor)
        square_size_branca = min(self.width() // 8, 0.6 * self.height() // 4)

        # Posições dos quadrados (ajustadas para ficarem mais próximas e centralizadas)

        square_positions = [
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + self.height() // 10 - square_size_branca // 2, square_size_branca, square_size_branca),
            (self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
            (3 * self.width() // 4 - square_size_branca // 2, 0.2 * self.height() + 9 * self.height() // 20 - square_size_branca // 2, square_size_branca, square_size_branca),
        ]

        # Desenhar quatro quadrados brancos na parte branca
        for (x, y, width, height), image in zip(square_positions, self.images):
            pen_branca = QPen(white)  # Configurar a caneta com cor branca e alpha 0 para tornar as bordas transparentes
            painter.setPen(pen_branca)
            painter.setBrush(white)
            painter.drawRect(x, y, width, height)
            painter.drawPixmap(x, y, width, height, image)

