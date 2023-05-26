import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'senha123',
  'host': '3.104.32.108',
  'database': 'africa_df'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
# Fechar a conexão
conn.close()

cursor = conn.cursor()

# Pedindo ao usuário o nome e código do estado
ID_animal = int(input("Digite o ID do novo animal: "))
raca = input("Digite o nome da raça: ")
quant = int(input("Digite a quantidade de animais: "))
risco_extin = input("Digite se possui risco de extinção (sim / não):  ")
local_animal = input("Digite a região em que foi encontrado o animal (norte, sul, leste ou oeste)")
# Inserindo o estado na tabela
sql = "INSERT INTO africa (ID_animal, raca, quant, risco_extin, local_animal) VALUES (%s, %s, %s, %s, %s)"
val = (ID_animal, raca, quant, risco_extin, local_animal)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()