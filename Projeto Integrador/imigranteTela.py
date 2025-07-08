import os
from imigrante import NovoImigrante, ListarImigrantes, DetalheImigrante, AlterarImigrante, DeletaImigrante


def Limpa_Tela():
    # Limpa a tela do terminal
    os.system("cls" if os.name == "nt" else "clear")


def MenuImigrante():
    while True:
        # Limpando a tela
        Limpa_Tela()
        # Criando o menu principal
        print("============== Menu Imigrante ==============")
        print("1. Cadastrar Imigrante")
        print("2. Listar Imigrante")
        print("3. Ver detalhe do imigrante")
        print("4. Alterar Imigrante")
        print("5. Deletar Imigrante")
        print("6. Sair")
        print("============================================")
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            # chamando metodo para cadastrar imigrante
            NovoImigrante()
        elif escolha == "2":
            # chamando metodo para listar todos os imigrantes
            ListarImigrantes()
            input("Pressione Enter para continuar...")
        elif escolha == "3":
            # chamando metodo que lista todos os imigrantes para que o usuário possa escolher um
            ListarImigrantes()
            id = input("Digite o ID do imigrante para ver os detalhes: ")
            Limpa_Tela()
            # chamando metodo para ver detalhes do imigrante
            DetalheImigrante(id)
        elif escolha == "4":
            #chamando o metodo para listar todos os imigrantes para escolher um imigrante
            ListarImigrantes()
            id = input("Digite o ID do imigrante que deseja alterar: ")
            Limpa_Tela()
            # chamando o metodo para alterar o imigrante
            AlterarImigrante(id)
        elif escolha == "5":
            #cchamando metodo para deletar imigrante
            ListarImigrantes()
            id = input("Digite o ID do imigrante que deseja deletar: ")
            Limpa_Tela()
            DeletaImigrante(id)
        elif escolha == "6":
            print("Voltando ao menu principal...")
            break