import os
from imigranteTela import MenuImigrante
from servicoTela import MenuServico


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
        print("2. Informação Complementar do Imigrante")
        print("3. Serviços de Apoio")
        print("4. Sair")
        print("============================================")
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            MenuImigrante()
        elif escolha == "2":
            print("Você escolheu Informação Complementar do Imigrante.")
        elif escolha == "3":
            MenuServico()
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break


if __name__ == "__main__":
    Menu()
