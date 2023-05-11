import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="rms-mysql.czcybmpf7emh.us-east-1.rds.amazonaws.com",
        user="admin",
        password="senha123",
        database="brasil"
    )
    return mydb