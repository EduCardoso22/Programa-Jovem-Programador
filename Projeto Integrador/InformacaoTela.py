import os
from Informacao import NovaInformacao, AlterarInformacao, ExcluirInformacao, ListarInformacao
from imigrante import DetalheImigrante
def Limpa_Tela():
    # Limpa a tela do terminal
    os.system("cls" if os.name == "nt" else "clear")
    
def MenuInformacao(idImigrante):
    while True:
        Limpa_Tela()

        DetalheImigrante(idImigrante)  # Exibe os detalhes do imigrante selecionado
        ListarInformacao(idImigrante)

        print("============== Menu Informação ==============")
        print("1. Cadastrar Informação Complementar")
        print("2. Alterar Informação Complementar")
        print("3. Excluir Informação Complementar")
        print("4. Listar Informações Complementares")
        print("5. Sair")
        print("=============================================")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            # chamando metodo para cadastrar informação
            NovaInformacao(idImigrante)
        
        elif escolha == "2":
            # chamando metodo para alterar informação
            AlterarInformacao() 
        
        elif escolha == "3":
            # chamando metodo para excluir informação
            ExcluirInformacao()
        
        elif escolha == "4":
            # chamando metodo para listar informações
            ListarInformacao(idImigrante)
        
        elif escolha == "5":
            print("Voltando ao menu principal...")
            return

        else:
            print("Opção inválida. Tente novamente.")
            MenuInformacao()
