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
from connection import Database
from aluno import Aluno
from ticket import Ticket
from config import Config
from pix import PixPage
from compras1 import compraCartao
class MainWindow(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget(self)
        self.db = Database()
        self.db.connect()
        self.db.create_tables()
        self.db.inserir_aluno('100100100-25', 'Renzo Tognella De Rosa', 45, '2413949', 'BSI')
        pratos_dia = [
            'Batata Assada com camarão e repolho ao molho barbecue',
            'Macarrao com picanha australiana acompanhado de farofa',
            'Risotto de frango chines com gorgonzola',
            'Pure de batata com cordeiro',
            'Feijoada do chef',
            'Pizza a moda do RU'
        ]
        pratos_noite = [
            'Macarrao com picanha australiana acompanhado de farofa',
            'Batata Assada com camarão e repolho ao molho barbecue',
            'Pure de batata com cordeiro',
            'Pizza a moda do RU',
            'Feijoada do chef',
            'Feijoada do chef'
        ]
        self.db.inserir_prato_cardapiodia(*pratos_dia)
        self.db.inserir_prato_cardapionoite(*pratos_noite)


        # Criar instâncias das telasr
        self.aluno = Aluno
        self.tela_inicial = TelaInicial()
        self.tela_login = telaDeLogin()
        self.tela_menu = telaMenu()
        self.tela_escolha_pag = telaEscolhaPag()
        self.tela_cardapio = cardapioTela()
        self.historico = HistoricocomprasApp()
        self.Conta = ContaApp()
        self.config = Config()
        self.pix = PixPage()
        self.cartao = compraCartao()
        # Adicionar as telas ao QStackedWidget
        self.stacked_widget.addWidget(self.tela_menu)
        self.stacked_widget.addWidget(self.tela_inicial)
        self.stacked_widget.addWidget(self.tela_login)
        self.stacked_widget.addWidget(self.tela_escolha_pag)
        self.stacked_widget.addWidget(self.tela_cardapio)
        self.stacked_widget.addWidget(self.historico)
        self.stacked_widget.addWidget(self.Conta)
        self.stacked_widget.addWidget(self.config)
        self.stacked_widget.addWidget(self.pix)
        self.stacked_widget.addWidget(self.cartao)

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
        self.historico.buttonConfirmar.clicked.connect(self.atualizarHistorico)
        self.Conta.botao_voltar.clicked.connect(self.voltar_tela_menu)
        self.tela_cardapio.botao_voltar.clicked.connect(self.voltar_tela_menu)
        self.tela_escolha_pag.botao_voltar.clicked.connect(self.voltar_tela_menu)
        self.historico.botao_voltar.clicked.connect(self.voltar_tela_menu)
        self.tela_menu.buttonEngrenagem.clicked.connect(self.mostrarConfig)
        self.config.botao_sair.clicked.connect(self.voltarTelaLogin)
        self.config.botao_voltar.clicked.connect(self.voltar_tela_menu)
        self.pix.botao_voltar.clicked.connect(self.voltar_tela_pag)
        self.cartao.botao_voltar.clicked.connect(self.voltar_tela_pag)
        self.tela_escolha_pag.botao_cartao.clicked.connect(self.mostraTelaCartao)
        self.tela_escolha_pag.botao_pix.clicked.connect(self.mostraTelaPix)
        self.pix.botao_comprar.clicked.connect(self.adicionarSaldo)
    def adicionarSaldo(self):
        valor = float(self.pix.edit_valor.text())
        saldo = float(self.aluno.saldo) + valor
        query = f"UPDATE pessoa SET saldo = {saldo} WHERE pessoa.cpf = '{self.aluno.cpf}'"
        self.db.execute_queryUpdate(query)
        self.aluno.saldo = saldo
        self.voltar_tela_menu()
    def mostraTelaCartao(self):
        self.stacked_widget.setCurrentWidget(self.cartao)
    def mostraTelaPix(self):
        self.stacked_widget.setCurrentWidget(self.pix)
    def voltarTelaLogin(self):
        self.stacked_widget.setCurrentWidget(self.tela_login)
        self.aluno = None
    def mostrarConfig(self):
        self.stacked_widget.setCurrentWidget(self.config)
    def voltar_tela_menu(self):
        self.stacked_widget.setCurrentWidget(self.tela_menu)
    def voltar_tela_pag(self):
        self.stacked_widget.setCurrentWidget(self.tela_escolha_pag)
    def mostrar_tela_menu(self):
        query = "select RA from aluno where RA = " + self.tela_login.text_ra.text()
        resultado = self.db.execute_query(query)
        resultado = resultado[0][0]
        resultado1 = self.tela_login.text_ra.text()
        if int(resultado1) == int(resultado):   
            resultadoX = self.tela_login.text_senha.text()
            query1 = "SELECT cpf FROM pessoa WHERE cpf = '" + resultadoX + "'"
            self.resultado2 = self.db.execute_query(query1)
            (self.resultadoFinal,) = self.resultado2[0]
            if self.resultadoFinal == resultadoX: 
                self.aluno = self.db.obter_info_pessoa_por_cpf(self.resultadoFinal)
                self.stacked_widget.setCurrentWidget(self.tela_menu)
            self.tela_login.label_senha.setStyleSheet('color: red')
        self.tela_login.label_senha.setStyleSheet('color: red')          

    def mostrar_tela_cardapio(self):
        self.stacked_widget.setCurrentWidget(self.tela_cardapio)
        query = "SELECT * FROM cardapiodia limit 1"
        resultado = self.db.execute_query(query)
        self.tela_cardapio.labels_almoco[0].setText("Segunda: " + str(resultado[0][0]))
        self.tela_cardapio.labels_almoco[1].setText("Terça: " + str(resultado[0][1]))
        self.tela_cardapio.labels_almoco[2].setText("Quarta: " + str(resultado[0][2]))
        self.tela_cardapio.labels_almoco[3].setText("Quinta: " + str(resultado[0][3]))
        self.tela_cardapio.labels_almoco[4].setText("Sexta: " + str(resultado[0][4]))
        self.tela_cardapio.labels_almoco[5].setText("Sabado: " + str(resultado[0][5]))
        self.stacked_widget.setCurrentWidget(self.tela_cardapio)
        query = "SELECT * FROM cardapionoite limit 1"
        resultado = self.db.execute_query(query)
        self.tela_cardapio.labels_jantar[0].setText("Segunda: " + str(resultado[0][0]))
        self.tela_cardapio.labels_jantar[1].setText("Terça: " + str(resultado[0][1]))
        self.tela_cardapio.labels_jantar[2].setText("Quarta: " + str(resultado[0][2]))
        self.tela_cardapio.labels_jantar[3].setText("Quinta: " + str(resultado[0][3]))
        self.tela_cardapio.labels_jantar[4].setText("Sexta: " + str(resultado[0][4]))
        self.tela_cardapio.labels_jantar[5].setText("Sabado: " + str(resultado[0][5]))
    def mostrar_tela_EscolhaPag(self):
        self.tela_escolha_pag.label_valor.setText(str(self.aluno.saldo))
        self.stacked_widget.setCurrentWidget(self.tela_escolha_pag)    
    def mostrar_tela_historico(self):
        self.stacked_widget.setCurrentWidget(self.historico)        
    def mostrar_tela_conta(self):
        self.stacked_widget.setCurrentWidget(self.Conta) 
        self.Conta.gerar_codigo_barras(self.aluno.nome, self.aluno.curso, self.aluno.ra)           
        self.Conta.nome_usuario.setText(self.aluno.nome)    
        self.Conta.departamento.setText(self.aluno.curso)
        self.Conta.ra.setText(str(self.aluno.ra))
    def atualizarHistorico(self):
        resultado = self.historico.text.text() 
        query = "SELECT dia, horario, ticket_id, cpf_pessoa, usado FROM ticket where     dia = " + "'" + resultado + "'" + "and cpf_pessoa = " + "'" + self.aluno.cpf  + "'"
        resultado = self.db.execute_query(query)
        if resultado:
            self.ticket1 = Ticket(dia=resultado[0][0], horario= resultado[0][1], ticket_id= resultado[0][2], cpf_pessoa= resultado[0][3], usado= resultado[0][4])
            self.ticket2 = Ticket(dia=resultado[1][0], horario= resultado[1][1], ticket_id= resultado[1][2], cpf_pessoa= resultado[1][3], usado= resultado[1][4])
            self.historico.label1.setText("Refeição do ticket foi comprada no horario: " + str(self.ticket1.horario) + " Esse ticket é o de numero: " + str(self.ticket1.ticket_id))
            self.historico.label2.setText("Refeição do ticket foi comprada no horario: " + str(self.ticket2.horario) + " Esse ticket é o de numero: " + str(self.ticket2.ticket_id))
if __name__ == "__main__":  
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
    