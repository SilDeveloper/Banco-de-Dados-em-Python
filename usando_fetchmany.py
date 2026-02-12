import sqlite3

# Conecta ao banco
conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor() # Auxiliar p/ fazer qualquer ação no banco de dados

# Criar tabela agendamentos
cursor.execute('''
               CREATE TABLE IF NOT EXISTS agendamentos
               (id INTEGER PRIMARY KEY, 
               nome TEXT NOT NULL,
               data TEXT,
               horario TEXT)
               
''')

# Inserir agendamentos
#1
cursor.execute('''
               INSERT INTO agendamentos
               (nome, data, horario) VALUES
               ('Ana','12/01/2026','11:00')           
''')
#2
cursor.execute('''
               INSERT INTO agendamentos
               (nome, data, horario) VALUES
               ('Beto','13/01/2026','14:00')    
''')
#3
cursor.execute('''
               INSERT INTO agendamentos
               (nome, data, horario) VALUES
               ('Carla','25/02/2026','09:00')
''')

# Faz o SELECT que seleciona tudo da tabela agendamentos
cursor.execute('SELECT * FROM agendamentos')

# FETCHMANY que retorna uma quantidade de linhas/tuplas da tabela
agendamentos = cursor.fetchmany(3)

for agendamento in agendamentos:
    print(agendamento)

conexao.commit()

# Fecha a conexão
conexao.close()
