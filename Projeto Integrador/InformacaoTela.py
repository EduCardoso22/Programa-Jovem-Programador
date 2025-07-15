import os
from servico import NovoServico, ListarServicos, DetalheServico, AlterarServico, DeletaServico

def Limpa_Tela():
    # Limpa a tela do terminal
    os.system("cls" if os.name == "nt" else "clear")

def MenuInformacao():
    Limpa_Tela()

    print("============== Menu Informação ==============")
    print("1. Cadastrar Informação Complementar")
    print("2. Alterar Informação Complementar")
    print("3. Excluir Informação Complementar")
    print("4. Sair")
    print("=============================================")

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == "1":
        # chamando metodo para cadastrar informação
        NovaInformacao()
    
    elif escolha == "2":
        # chamando metodo para alterar informação
        AlterarInformacao() 
    
    elif escolha == "3":
        # chamando metodo para excluir informação
        ExcluirInformacao()
    
    elif escolha == "4":
        print("Voltando ao menu principal...")
        break

    else:
        print("Opção inválida. Tente novamente.")
        MenuInformacao()
