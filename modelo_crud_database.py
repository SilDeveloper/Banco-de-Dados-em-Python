'''
CRUD:

CREATE
READ
UPDATE
DELETE
'''

import sqlite3

# a) Conecte-se a um banco de dados chamado empresa.db
conexao = sqlite3.connect('empresa.db')
print('Conexao bem sucedida')
cursor = conexao.cursor()

# b) Crie uma tabela chamada funcionarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    SALARIO REAL
);
""")
print('Tabela FUNCIONARIOS pronta.')


# Inserindo 2 funcionários usando placeholders (Lista com Tuplas)
novos_funcionarios = [
    ("Clara Souza", 5500.00),
    ("Raissa Mendes", 4200.00)
]

# INSERT usando '?' como placeholders
sql_insert_command = """
INSERT INTO FUNCIONARIOS (NOME, SALARIO) VALUES (?, ?);
"""

#tente
try:
    cursor.executemany(sql_insert_command, novos_funcionarios)
    
    # 4. Confirmamos a operação no banco de dados (commit)
    conexao.commit()
    
    print(f'Inseridos {cursor.rowcount} funcionários com sucesso!')

# exceção
except sqlite3.Error as e:
    print(f"Ocorreu um erro ao inserir dados: {e}")


# Verificação
print("\nVerificando dados na tabela:")
cursor.execute("SELECT NOME, SALARIO FROM FUNCIONARIOS;")
registros = cursor.fetchall()
for row in registros:
    print(row)


# Fechar conexão
cursor.close()
conexao.close()
