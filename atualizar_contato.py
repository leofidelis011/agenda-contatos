
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def atualizar_contato():
    while True:
        try:
            id_contato = int(input("Digite o ID do contato que deseja atualizar: "))
            if id_contato >0:
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
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * FROM contatos
                    WHERE id = %s
                    """,
                    (id_contato,)
                )
                contatos = cursor.fetchone()
                if contatos is None:
                    print("O contato não existe!")
                else:
                    print("Coloque os novos dados!")

                    novo_nome = input("Digite o seu nome: ")
                    novo_telefone = input("Digite o seu telefone: ")
                    novo_email = input("Digite o seu email: ")
                
                    cursor.execute(
                        """
                        UPDATE contatos
                        SET nome = %s,
                            telefone = %s,
                            email = %s
                        WHERE id = %s
                        """,
                        (novo_nome, novo_telefone, novo_email, id_contato,)
                    )
                    linha = cursor.rowcount
                    if linha > 0:
                        print("O contato foi atualizado com sucesso!")
                    else:
                        print("Nenhum contato foi atualizado!")
    except psycopg.errors.UniqueViolation:
        print("Esse telefone ou e-mail já pertence a outro contato")
    except psycopg.Error:
        print("Erro ao realizar a operação no banco de dados!")