import sqlite3
from sqlite3 import Error
import hashlib
import os

DATABASE = "/tmp/teste_sqlite.db"
"""
ATENÇÃO: Este código é propositalmente vulnerável,
para fins de estudo de programação segura
--------------------------------------------------
TCC CyberSecurity PucPR 1Sem2019
"""


def passwd_hash(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()


class BancoTeste:
    def __init__(self):
        self.conn = None
        self.db = DATABASE

    def criar_conexao(self):
        try:
            self.conn = sqlite3.connect(self.db)
        except Error as e:
            print(e)
        return self.conn

    def criar_tabela(self, criar_tabela_sql):

        try:
            c = self.conn.cursor()
            c.execute(criar_tabela_sql)
        except Error as e:
            print(e)

    def criar_banco(self):

        sql_criar_projetos_table = """ CREATE TABLE IF NOT EXISTS projetos (
                                            id integer PRIMARY KEY,
                                            nome text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """
        sql_criar_usuarios_table = """ CREATE TABLE IF NOT EXISTS usuarios (
                                            id integer PRIMARY KEY,
                                            usuario text NOT NULL,
                                            passwd text,
                                            admin boolean,
                                            create_date text
                                        ); """

        sql_criar_tarefas_table = """CREATE TABLE IF NOT EXISTS tarefas (
                                        id integer PRIMARY KEY,
                                        nome text NOT NULL,
                                        prioridade integer,
                                        status_id integer NOT NULL,
                                        projeto_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (projeto_id) REFERENCES projetos (id)
                                    );"""

        # create a database connection
        self.criar_conexao()

        # create tables
        if self.conn is not None:
            self.criar_tabela(sql_criar_projetos_table)
            self.criar_tabela(sql_criar_usuarios_table)
            self.criar_tabela(sql_criar_tarefas_table)
        else:
            print("Error! Impossivel criar a base de dados.")

    def criar_projeto(self, projeto):

        sql = ''' INSERT INTO projetos(nome,begin_date,end_date)
                  VALUES(?,?,?) '''
        cursor = self.conn.cursor()
        cursor.execute(sql, projeto)
        self.conn.commit()
        return cursor.lastrowid

    def criar_tarefa(self, tarefa):

        sql = ''' INSERT INTO tarefas(nome,prioridade,status_id,projeto_id,begin_date,end_date) VALUES (?,?,?,?,?,?) 
        '''
        cur = self.conn.cursor()
        cur.execute(sql, tarefa)
        self.conn.commit()
        return cur.lastrowid

    def criar_usuario(self, dados_usuario):

        sql = ''' INSERT INTO usuarios(usuario,passwd,admin,create_date) VALUES (?,?,?,?) 
        '''
        cur = self.conn.cursor()
        cur.execute(sql, dados_usuario)
        self.conn.commit()
        return cur.lastrowid

    def validar_admin(self, usuario: str) -> bool:
        self.criar_conexao()
        admin = False
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT admin FROM usuarios WHERE usuario = '%s'" % usuario)
            admin = cursor.fetchone()
        return admin

    def obter_hash(self, usuario: str):
        self.criar_conexao()
        valor = None
        cursor = self.conn.cursor()
        cursor.execute("SELECT passwd FROM usuarios WHERE usuario = '%s'" % usuario)
        valor = cursor.fetchone()
        return valor

    def pesquisar_projetos_nome(self, nome=None):
        self.criar_conexao()
        cursor = self.conn.cursor()
        projs = None
        cursor.execute(
            "SELECT * FROM projetos WHERE nome LIKE '%" + nome + "%'")
        projs = cursor.fetchall()
        return projs

    def pesquisar_projeto(self, projeto_id=0):
        self.criar_conexao()
        cursor = self.conn.cursor()
        proj = None
        cursor.execute("SELECT * FROM projetos WHERE id = " + str(projeto_id))
        proj = cursor.fetchone()
        return proj

    def listar_projetos(self):
        self.criar_conexao()
        cursor = self.conn.cursor()
        projs = ()
        cursor.execute("SELECT * FROM projetos")
        projs = cursor.fetchall()
        return projs

    def pesquisar_tarefas_projeto(self, projeto_id=0):
        self.criar_conexao()
        tarefas = ()
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM tarefas WHERE projeto_id = " + str(projeto_id))
        print("SELECT * FROM tarefas WHERE projeto_id = " + str(projeto_id))
        tarefas = cursor.fetchall()
        return tarefas


if __name__ == '__main__':
    banco = BancoTeste()
    if not os.path.isfile(DATABASE):
        banco.criar_banco()
        banco.criar_conexao()
        # carga de exemplos
        usuarios = (
            ('admin', passwd_hash('Admin123'), True, '2021-04-22'),
            ('teste', passwd_hash('TesteSistema'), True, '2021-04-22'),
            ('joao', passwd_hash('Brasil1970'), True, '2021-04-22'),
            ('maria', passwd_hash('987654321'), True, '2021-04-22'),
        )
        for usuario in usuarios:
            banco.criar_usuario(usuario)

        projeto = ('Novo aplicativo seguro', '2021-01-01', '2021-01-30')
        projeto_id = banco.criar_projeto(projeto)
        tarefas = (
            ('Analise de requisitos', 1,
             1, projeto_id, '2021-01-01', '2021-01-02'),
            ('Confirmar com gerente as etapas',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
        )
        for tarefa in tarefas:
            banco.criar_tarefa(tarefa)

        projeto = ('Novo teste de dados', '2021-02-01', '2021-02-30')
        projeto_id = banco.criar_projeto(projeto)
        tarefas = (
            ('Projeto de testes', 1,
             1, projeto_id, '2021-01-01', '2021-01-02'),
            ('Confirmar checklist com time de dev',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
            ('Confirmar checklist com time de dev',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
        )
        for tarefa in tarefas:
            banco.criar_tarefa(tarefa)

        projeto = ('Migração de base de dados', '2021-01-01', '2021-01-30')
        projeto_id = banco.criar_projeto(projeto)
        tarefas = (
            ('Testes de exportação de dados', 1,
             1, projeto_id, '2021-01-01', '2021-01-02'),
            ('Testes de importação de dados',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
            ('Ajustes de performance',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
        )
        for tarefa in tarefas:
            banco.criar_tarefa(tarefa)

        projeto = ('renovação do parque tecnológico', '2021-01-01', '2021-01-30')
        projeto_id = banco.criar_projeto(projeto)
        tarefas = (
            ('Cotação de preços com fornecedores', 1,
             1, projeto_id, '2021-01-01', '2021-01-02'),
            ('Revisão de inventário',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
            ('Verificação para revenda do hardware antigo',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
            ('Cotação de contrato de manutenção predial',
             1, 1, projeto_id, '2021-01-03', '2021-01-05'),
        )
        for tarefa in tarefas:
            banco.criar_tarefa(tarefa)
