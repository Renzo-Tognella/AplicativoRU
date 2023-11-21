import mysql.connector
from aluno import Aluno
class Database:

    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'renzo123',
            'host': 'localhost',
            'database': 'ruapplication',
        }
        self.conn = None
        self.cursor = None
    
    def create_tables(self):
        # Criação da tabela pessoa
        query = """
            CREATE TABLE IF NOT EXISTS pessoa (
                cpf VARCHAR(15) PRIMARY KEY,
                nome VARCHAR(45),
                saldo FLOAT
            )
        """
        self.execute_query(query)

        # Criação da tabela aluno
        query = """
            CREATE TABLE IF NOT EXISTS aluno (
                RA INT PRIMARY KEY,
                cpf VARCHAR(45),
                curso VARCHAR(45),
                FOREIGN KEY (cpf) REFERENCES pessoa(cpf)
            )
        """
        self.execute_query(query)

        # Criação da tabela ticket
        query = """
            CREATE TABLE IF NOT EXISTS ticket (
                ticket_id INT AUTO_INCREMENT PRIMARY KEY,
                usado TINYINT(1),
                dia DATE,
                cpf_pessoa VARCHAR(15),
                horario TIME,
                FOREIGN KEY (cpf_pessoa) REFERENCES pessoa(cpf)
            )
        """
        self.execute_query(query)

        # Criação da tabela funcionario
        query = """
            CREATE TABLE IF NOT EXISTS funcionario (
                cpf VARCHAR(50) PRIMARY KEY,
                cargo VARCHAR(45),
                RA VARCHAR(45) PRIMARY KEY,
                FOREIGN KEY (cpf) REFERENCES pessoa(cpf)
            )
        """
        self.execute_query(query)

        # Criação da tabela cardapiodia
        query = """
            CREATE TABLE IF NOT EXISTS cardapiodia (
                segunda VARCHAR(100),
                terca VARCHAR(100),
                quarta VARCHAR(100),
                quinta VARCHAR(100),
                sexta VARCHAR(100),
                sabado VARCHAR(100)
            )
        """
        self.execute_query(query)

        # Criação da tabela cardapionoite
        query = """
            CREATE TABLE IF NOT EXISTS cardapionoite (
                segunda VARCHAR(100),
                terca VARCHAR(100),
                quarta VARCHAR(100),
                quinta VARCHAR(100),
                sexta VARCHAR(100),
                sabado VARCHAR(100)
            )
        """
        self.execute_query(query)
    def inserir_aluno(self, cpf, nome, saldo, RA, curso):
        # Verificar se o CPF já existe na tabela pessoa
        cpf_existente = self.verificar_cpf_existente(cpf)

        if cpf_existente:
            print(f"O CPF {cpf} já está cadastrado.")
            return

        # Verificar se o RA já existe na tabela aluno
        ra_existente = self.verificar_ra_existente(RA)

        if ra_existente:
            print(f"O RA {RA} já está cadastrado.")
            return

        # Inserir dados na tabela pessoa
        query_pessoa = f"""
            INSERT INTO pessoa (cpf, nome, saldo)
            VALUES ('{cpf}', '{nome}', {saldo})
        """
        self.execute_query(query_pessoa)

        # Inserir dados na tabela aluno
        query_aluno = f"""
            INSERT INTO aluno (RA, cpf, curso)
            VALUES ({RA}, '{cpf}', '{curso}')
        """
        self.execute_query(query_aluno)
        self.inserir_ticket('100100100-25', '2023-11-28', '1', '19:34:56')
        self.inserir_ticket('100100100-25', '2023-11-28', '1', '13:34:56')


    def verificar_cpf_existente(self, cpf):
        # Verificar se o CPF já existe na tabela pessoa
        query = f"SELECT cpf FROM pessoa WHERE cpf = '{cpf}'"
        resultado = self.execute_query(query)
        return bool(resultado)

    def verificar_ra_existente(self, RA):
        # Verificar se o RA já existe na tabela aluno
        query = f"SELECT RA FROM aluno WHERE RA = {RA}"
        resultado = self.execute_query(query)
        return bool(resultado)
    def inserir_prato_cardapiodia(self, *pratos):
        # Inserir prato no cardápio do dia
        pratos_str = "', '".join(pratos)
        query = f"""
            INSERT INTO cardapiodia (segunda, terca, quarta, quinta, sexta, sabado)
            VALUES ('{pratos_str}')
        """
        self.execute_query(query)
    def inserir_prato_cardapionoite(self, *pratos):
        # Inserir prato no cardápio do dia
        pratos_str = "', '".join(pratos)
        query = f"""
            INSERT INTO cardapiodia (segunda, terca, quarta, quinta, sexta, sabado)
            VALUES ('{pratos_str}')
        """
        self.execute_query(query)

    def inserir_ticket(self, cpf_pessoa, dia, usado, horario):
        # Inserir um novo ticket na tabela 'ticket'
        query = f"INSERT INTO ticket (usado, dia, cpf_pessoa, horario) VALUES ({usado}, '{dia}', '{cpf_pessoa}', '{horario}')"
        return self.execute_query(query)
    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            print("Conexão bem-sucedida!")
        except mysql.connector.Error as err:
            print(f"Erro na conexão: {err}")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print(f"Erro na execução da consulta: {err}")
            return None
    def execute_queryUpdate(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()  
            print("Consulta executada com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro na execução da consulta: {err}")    

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")
            
    def obter_info_pessoa_por_cpf(self, cpf):
        query = f"SELECT pessoa.cpf, pessoa.nome, pessoa.saldo, aluno.ra, aluno.curso FROM aluno JOIN pessoa ON aluno.cpf = pessoa.cpf WHERE pessoa.cpf = '{cpf}'"

        self.cursor.execute(query)
        resultado = self.cursor.fetchone()

        if resultado:
            if len(resultado) >= 5:
                cpf, nome, saldo, ra, curso = resultado
                pessoa = Aluno(cpf, nome, saldo, ra, curso)
                return pessoa
            else:
                print("Erro: Resultado da consulta não possui elementos suficientes.")
                return None
        else:
            print(f"Nenhuma pessoa encontrada com CPF {cpf}")
            return None