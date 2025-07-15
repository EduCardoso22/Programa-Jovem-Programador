from conn import Conectar

def NovaInformacao(IdImigrante):
    print("===================================")
    print("Cadastro de Informação Complementar")
    print("===================================")
    print("")

    tipo = input("Digite o tipo de informação: ")
    descricao = input("Digite a descrição da informação: ")
    ano_inicio = input("Digite o ano de início: ")
    ano_final = input("Digite o ano de fim (deixe em branco se não aplicável): ")