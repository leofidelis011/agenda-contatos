
import os 
import psycopg
from dotenv import load_dotenv

load_dotenv()

def excluir_contato():
    while True:
        try:
            id_contato = int(input("Digite o ID do contato que deseja excluir: "))
            if id_contato > 0:
                break
            else:
                print("Erro: O número deve ser maior que zero (não pode ser negativo nem 0).")
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
    try:
        with psycopg.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        ) as conn:
            while True:
                excluir = input("Tem certeza de que deseja excluir este contato? (s/n): ").lower()
                if excluir == "s":
                    with conn.cursor() as cursor:
                        cursor.execute(
                            """
                            DELETE FROM contatos
                            WHERE id = %s
                            """,
                            (id_contato,)
                        )
                        contatos = cursor.rowcount
                    if contatos > 0:
                        print("Exclusão concluída com sucesso!")
                    else:
                        print("Nenhum registro correspondente foi excluído.")
                    break
                elif excluir == "n":
                    print("Operação cancelada.")
                    break
                else:
                    print("Digite 's' ou 'n'!")
    except psycopg.Error:
        print("Erro ao realizar a operação no banco de dados!")