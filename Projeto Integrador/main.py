import os
from imigranteTela import MenuImigrante
from servicoTela import MenuServico
from InformacaoTela import MenuInformacao


def Limpa_Tela():
    # Limpa a tela do terminal
    os.system("cls" if os.name == "nt" else "clear")


def Menu():
    while True:
        # Limpando a tela
        Limpa_Tela()
        # Criando o menu principal
        print("============== Menu Principal ==============")
        print("1. Imigrante")
        print("2. Serviços de Apoio")
        print("3. Sair")
        print("============================================")
        escolha = input("Escolha uma opção (1-3): ")

        if escolha == "1":
            MenuImigrante()
        elif escolha == "2":
            MenuServico()
        elif escolha == "3":
            print("Saindo do programa. Até logo!")
            


if __name__ == "__main__":
    Menu()
