
import os
import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

def buscar_contato():
    busca = input("Digite o nome ou telefone do contato: ")
    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:
            with conn.cursor(row_factory=dict_row) as cursor:
            # 1. Execute uma consulta SQL para buscar o contato.
                cursor.execute(
                    "SELECT * FROM contatos WHERE nome = %s OR telefone = %s",
                    (busca, busca,)            
                )
            # 2. Recupere o resultado encontrado.
                contatos = cursor.fetchone()
            # 3. Verifique se o contato existe.
                if contatos is None:
                    print("Nenhum contato encontrado.")
            # 4. Exiba os dados do contato.
                else:
                    print(f"ID: {contatos['id']} | Nome: {contatos['nome']} | "
                        f"Telefone: {contatos['telefone']} | Email: {contatos['email']}")
    except psycopg.Error:
        print("Erro ao realizar a operação no banco de dados!")