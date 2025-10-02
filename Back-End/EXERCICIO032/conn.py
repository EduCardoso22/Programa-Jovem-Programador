import mysql.connector
from mysql.connector import errorcode

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="controle_gastos" 
        )
        return conexao
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Erro de acesso: verifique seu nome de usuário ou senha.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("O banco de dados especificado não existe.")
        else:
            print(f"Ocorreu um erro ao conectar: {err}")
        return None