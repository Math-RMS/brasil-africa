import mysql.connector

# Conectando ao banco de dados
config = {
  'user': 'admin',
  'password': 'senha123',
  'host': 'rms-mysql.czcybmpf7emh.us-east-1.rds.amazonaws.com',
  'database': 'brasil'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# Pedindo ao usuário o nome e código do estado
ID_tribo = int(input("Digite o ID da nova tribo: "))
nome_tribo = input("Digite o nome da nova tribo: ")
num_habit = int(input("Digite o número de habitantes da tribo: "))
renda_mensal = input("Digite a renda mensal da tribo:  ")
escolariedade = input("Digite o nivel de escolareidade (fundamental, médio ou superior)")
trab_assa = input("Digite se possuem trabalho assalariado sim ou não: ")
# Inserindo o estado na tabela
sql = "INSERT INTO tb_brasil (ID_tribo, nome_tribo, num_habit, renda_mensal, escolariedade, trab_assa) VALUES (%s, %s, %s, %s, %s, %s)"
val = (ID_tribo, nome_tribo, num_habit, renda_mensal, escolariedade, trab_assa)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()