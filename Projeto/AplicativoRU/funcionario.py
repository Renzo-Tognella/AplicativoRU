from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, saldo, registro, cargo):
        super().__init__(cpf, nome, saldo)
        self.cargo = registro
        self.cargo = cargo