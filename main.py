
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def cadastrar_contato():
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu email: ")
    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:
            with conn.cursor() as cursor: 
                cursor.execute(
                    "INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)",
                        (nome, telefone, email)
                    )
                print("Contato cadastrado com sucesso!")
    except psycopg.errors.UniqueViolation:
        print("Este telefone ou e-mail já está cadastrado!")
    except psycopg.Error:
        print("Erro ao realizar a operação no banco de dados!")