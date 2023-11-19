import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QApplication
from tela_inicial import TelaInicial
from Tela_de_login import telaDeLogin
from menu import telaMenu
from escolhaDePagamento import telaEscolhaPag
from cardapio import cardapioTela
from historico import HistoricocomprasApp
from Conta import ContaApp
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget(self)

        # Criar instâncias das telas
        self.tela_inicial = TelaInicial()
        self.tela_login = telaDeLogin()
        self.tela_menu = telaMenu()
        self.tela_escolha_pag = telaEscolhaPag()
        self.tela_cardapio = cardapioTela()
        self.historico = HistoricocomprasApp()
        self.Conta = ContaApp()

        # Adicionar as telas ao QStackedWidget
        self.stacked_widget.addWidget(self.tela_menu)
        self.stacked_widget.addWidget(self.tela_inicial)
        self.stacked_widget.addWidget(self.tela_login)
        self.stacked_widget.addWidget(self.tela_escolha_pag)
        self.stacked_widget.addWidget(self.tela_cardapio)
        self.stacked_widget.addWidget(self.historico)
        self.stacked_widget.addWidget(self.Conta)

        # Definir a tela inicial
        self.stacked_widget.setCurrentWidget(self.tela_login)

        # Configurar a central widget
        self.setCentralWidget(self.stacked_widget)

        # Conectar sinais para alternar entre as telas
        self.tela_login.button.clicked.connect(self.mostrar_tela_menu)
        self.tela_menu.buttonCardapio.clicked.connect(self.mostrar_tela_cardapio)
        self.tela_menu.buttonCompras.clicked.connect(self.mostrar_tela_EscolhaPag)
        self.tela_menu.buttonHistorico.clicked.connect(self.mostrar_tela_historico)
        self.tela_menu.buttonConta.clicked.connect(self.mostrar_tela_conta)

    def mostrar_tela_menu(self):
        self.stacked_widget.setCurrentWidget(self.tela_menu)
    def mostrar_tela_cardapio(self):
        self.stacked_widget.setCurrentWidget(self.tela_cardapio)
    def mostrar_tela_EscolhaPag(self):
        self.stacked_widget.setCurrentWidget(self.tela_escolha_pag)    
    def mostrar_tela_historico(self):
        self.stacked_widget.setCurrentWidget(self.historico)        
    def mostrar_tela_conta(self):
        self.stacked_widget.setCurrentWidget(self.Conta)               

if __name__ == "__main__":  
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
