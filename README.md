# Persistência de Dados com Python e SQLite3 🗄️

Este repositório contém implementações práticas para manipulação de bancos de dados relacionais utilizando Python. O foco aqui é demonstrar o uso da biblioteca nativa `sqlite3` para a criação de sistemas robustos, seguros e eficientes.

## 🛠️ Conceitos Aplicados
* **DML (Data Manipulation Language):** Inserção e consulta de registros de forma otimizada.
* **Segurança da Informação:** Uso de **Placeholders** (`?`) em consultas SQL para prevenir ataques de **SQL Injection**.
* **Tratamento de Exceções:** Implementação de blocos `try/except` para garantir a integridade das transações e o fechamento correto de conexões.
* **Transações Atomizadas:** Uso do método `commit()` para assegurar a persistência dos dados no banco local (`.db`).

## 📁 Estrutura do Projeto
Script com fluxo de aplicação de gestão:
1. Conexão com o banco de dados.
2. Definição do esquema da tabela (`CREATE TABLE IF NOT EXISTS`).
3. Inserção em lote (*Bulk Insert*) utilizando `executemany`.
4. Recuperação e exibição dos dados.

## 🚀 Por que SQLite3?
Optei pelo SQLite por ser um banco de dados *serverless* e autocontido, ideal para aplicações de modelagem computacional e prototipagem rápida, onde a simplicidade e a portabilidade são cruciais para a análise de dados.

---
**Silvia M.** | Licenciada em Computação (UFF)
