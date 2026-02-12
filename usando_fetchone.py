import sqlite3

# 1. Conecta ao banco de dados (será criado se não existir)
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

# 2. Cria a tabela (ID como Chave Primária com autoincremento)
cursor.execute('CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')

# 3. Limpa a tabela para o exemplo rodar "limpo" toda vez
cursor.execute('DELETE FROM alunos')

# 4. Reseta o contador de ID para começar do 1 novamente (Opcional, mas ajuda no exemplo)
cursor.execute("DELETE FROM sqlite_sequence WHERE name='alunos'")

# 5. Insere os dados especificando a coluna 'nome'
cursor.execute("INSERT INTO alunos (nome) VALUES ('Silvia')")
cursor.execute("INSERT INTO alunos (nome) VALUES ('Caua')")

# IMPORTANTE: Salva as alterações no banco
conexao.commit()

# 6. Faz o SELECT para buscar todos os alunos
cursor.execute('SELECT * FROM alunos')

# 7. Utiliza o fetchone() para pegar APENAS o 1º aluno da fila
# O fetchone() retorna uma tupla única: (1, 'Sil')
primeiro_aluno = cursor.fetchone()

# Exibe o resultado
print("Resultado do fetchone():")
print(primeiro_aluno)

'''
# Exibir somente o 2º, no caso Caua
# Pula 1 registro (OFFSET 1) e pega o próximo (LIMIT 1)
cursor.execute('SELECT * FROM alunos LIMIT 1 OFFSET 1')

segundo_aluno = cursor.fetchone()
print(segundo_aluno) # Saída: (2, 'Caua')
'''

# 8. Fecha a conexão
conexao.close()
