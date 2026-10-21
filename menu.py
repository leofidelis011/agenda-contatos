from main import cadastrar_contato
from listar_contatos import listar_contatos
from buscar_contato import buscar_contato
from atualizar_contato import atualizar_contato
from excluir_contato import excluir_contato

def mostrar_menu():
    print("""
    ===== AGENDA DE CONTATOS =====
    1 - Cadastrar contato
    2 - Listar contatos
    3 - Buscar contato
    4 - Atualizar contato
    5 - Excluir contato
    6 - Sair
    """)

    while True:
        try:
            digite = int(input("Digite uma opção de 1 a 6: "))
            if 1 <= digite <= 6:
                return digite
            else:
                print("Erro: O número deve estar entre 1 a 6.")
        except ValueError:
            print("Erro: Por favor, digite apenas números!")
def main():
    while True:
        opcao = mostrar_menu()
        if opcao == 1:
            print("Você escolheu cadastrar contato.")
            cadastrar_contato()
        elif opcao == 2:
            print("Você escolheu listar contatos.")
            listar_contatos()
        elif opcao == 3:
            print("Você escolheu buscar contato.")
            buscar_contato()
        elif opcao == 4:
            print("Você escolheu atualizar contato.")
            atualizar_contato()
        elif opcao == 5:
            print("Você escolheu excluir contato.")
            excluir_contato()
        elif opcao == 6:
            print("Encerrando o programa.")
            break
if __name__ == "__main__":
    main() 