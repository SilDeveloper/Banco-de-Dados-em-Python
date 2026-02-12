import sqlite3

'''
BANCO DE DADOS
'''

class Banco:
    def __init__(self): # Método construtor
        self.conn = None
        self.cursor = None

    def conectar(self): # Molde
        #conectar no banco 'missoes.db'
        self.conn = sqlite3.connect('missoes.db')
        self.cursor = self.conn.cursor()

    def desconectar(self):
        # fechar conexão
        self.conn = self.conn.close()

    def criar_tabela(self):
        # criar tabela missoes se não existir
        self.cursor.execute('''
               CREATE TABLE IF NOT EXISTS tabela
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               data TEXT,
               horario TEXT)
''')

    def inserir(self):
        self.cursor.execute(''' INSERT INTO tabela (nome,data,horario) VALUES
        ('Sil','20/07/99','16:45')
         ''')
        
        self.cursor.execute(''' INSERT INTO tabela (nome,data,horario) VALUES
        ('Teste','20/07/2009','06:45')
         ''')
        
    def visualizar(self):
        self.conn.commit()
        self.cursor.execute(''' SELECT * FROM tabela ''')

Bank = Banco()
Bank.conectar()
Bank.criar_tabela()
Bank.inserir()
Bank.visualizar()
Bank.desconectar()
