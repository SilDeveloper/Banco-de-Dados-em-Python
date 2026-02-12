import sqlite3

# Conecta ao banco
conexao = sqlite3.connect('agendinha.db')
cursor = conexao.cursor()

# 1. Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos
    (id INTEGER PRIMARY KEY, 
    nome TEXT NOT NULL,
    data TEXT,
    horario TEXT)
''')

# --- SOLUÇÃO PARA NÃO REPETIR: Apaga os dados antigos antes de inserir novos ---
cursor.execute('DELETE FROM agendamentos')

# 2. Inserir agendamentos
cursor.execute("INSERT INTO agendamentos (nome, data, horario) VALUES ('Ana','12/01/2026','11:00')")
cursor.execute("INSERT INTO agendamentos (nome, data, horario) VALUES ('Beto','13/01/2026','14:00')")
cursor.execute("INSERT INTO agendamentos (nome, data, horario) VALUES ('Carla','25/02/2026','09:00')")

'''
# Apaga apenas o agendamento que tiver o ID igual a 2
id_para_deletar = 2
cursor.execute('DELETE FROM agendamentos WHERE id = ?', (id_para_deletar,))
'''

# Salva as inserções
conexao.commit()

# 3. Faz o SELECT
cursor.execute('SELECT * FROM agendamentos')

# FETCHALL: Retorna TUDO o que foi encontrado no SELECT
agendamentos = cursor.fetchall()

# Exibe os resultados
print(f"Exibindo todos os {len(agendamentos)} registros:")
for agendamento in agendamentos:
    print(agendamento)

# Fecha a conexão
conexao.close()
