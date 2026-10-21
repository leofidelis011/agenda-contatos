
import os
import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()

def listar_contatos():

    try:    
        with psycopg.connect(        
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:
            print("Conexão estabelecida!")
            with conn.cursor(row_factory=dict_row) as cursor:
                cursor.execute(
                    "SELECT * FROM contatos"
                )
                contatos = cursor.fetchall()

                if not contatos:
                    print("Nenhum contato encontrado!")
                else:
                    for contato in contatos:
                        print(f"ID: {contato['id']} | Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")
    except psycopg.Error:
        print("Não houve uma conexão!")        