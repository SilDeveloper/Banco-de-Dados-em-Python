import sqlite3

conexao = sqlite3.connect('projetos.db')

print('Conexao bem sucedida')

# Permite executar comandos SQL
cursor = conexao.cursor()

# Define o comando SQL em uma string
sql_command = """
CREATE TABLE IF NOT EXISTS TAREFAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DESCRICAO TEXT NOT NULL,
    STATUS TEXT
);
"""

# Executa o comando SQL usando o cursor
cursor.execute(sql_command)

# Confirma a operação no banco de dados
conexao.commit()

print('Tabela TAREFAS criada com sucesso!')

# Fecha a conexão
conexao.close()
