import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'senha123',
  'host': '34.205.29.132',
  'database': 'africa'
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
ID_animal = int(input("Digite o ID de um novo animal: "))
raca = input("Digite o nome da raça: ")
quantidade = int(input("Digite a quantidade de animais: "))
risco_extin = input("Digite se possui risco de extinção (sim / não):  ")
localiz_animal = input("Digite a região em que foi encontrado o animal (norte, sul, leste ou oeste)")
# Inserindo o estado na tabela
sql = "INSERT INTO africa (ID_animal, raca, quantidade, risco_extin, localiz_animal) VALUES (%s, %s, %s, %s, %s)"
val = (ID_animal, raca, quantidade, risco_extin, localiz_animal)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()