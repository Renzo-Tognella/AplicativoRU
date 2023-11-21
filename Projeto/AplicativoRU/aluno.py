from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, cpf, nome, saldo, ra, curso):
        super().__init__(cpf, nome, saldo)
        self.ra = ra
        self.curso = curso
