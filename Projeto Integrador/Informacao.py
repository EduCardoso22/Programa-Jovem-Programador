from conn import Conectar

def NovaInformacao(IdImigrante):
    print("===================================")
    print("Cadastro de Informação Complementar")
    print("===================================")
    print("")

    tipo = input("Digite o tipo de informação: ")
    descricao = input("Digite a descrição da informação: ")
    ano_inicio = input("Digite o ano de início: ")
    ano_termino = input("Digite o ano de término (deixe em branco se não aplicável): ")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviar os dados para o banco de dados
    cursor.execute(
        "INSERT INTO INFORMACAO (IDIMIGRANTE, TIPO, DESCRICAO, ANO_INICIO, ANO_TERMINO) VALUES (%s, %s, %s, %s, %s)",
        (IdImigrante, tipo, descricao, ano_inicio, ano_termino)
    )
    conn.commit()

    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()

    print("Informação complementar cadastrada com sucesso!")

    input("Pressione Enter para continuar...")

def ListarInformacao(IdImigrante):
    print("")
    print("======================================")
    print("Listagem de Informações Complementares")
    print("======================================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()
    
    # consultar os dados no banco de dados
    cursor.execute(
        "SELECT IDINFORMACAO, TIPO, DESCRICAO, ANO_INICIO, ANO_TERMINO FROM INFORMACAO WHERE IDIMIGRANTE = %s",
        (IdImigrante,)
    )

    for id, tipo, descricao, ano_inicio, ano_termino in cursor.fetchall():
        print(f"ID: {id}")
        print(f"Tipo: {tipo}")
        print(f"Descrição: {descricao}")
        print(f"Ano de Início: {ano_inicio}")
        print(f"Ano de Término: {ano_termino if ano_termino else 'N/A'}")
        print("")

    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()

def AlterarInformacao():
    print("===================================")
    print("Alteração de Informação Complementar")
    print("===================================")
    print("")

    idInformacao = input("Digite o ID da informação que deseja alterar: ")
    tipo = input("Digite o novo tipo de informação: ")
    descricao = input("Digite a nova descrição da informação: ")
    ano_inicio = input("Digite o novo ano de início: ")
    ano_termino = input("Digite o novo ano de término (deixe em branco se não aplicável): ")
    if not ano_termino:
        ano_termino = None
    
    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # atualizar os dados no banco de dados
    cursor.execute(
        "UPDATE INFORMACAO SET TIPO = %s, DESCRICAO = %s, ANO_INICIO = %s, ANO_TERMINO = %s WHERE IDINFORMACAO = %s",
        (tipo, descricao, ano_inicio, ano_termino, idInformacao)
    )
    conn.commit()
    print("Informação complementar alterada com sucesso!")

    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()

    input("Pressione Enter para continuar...")

def ExcluirInformacao():
    print("===================================")
    print("Exclusão de Informação Complementar")
    print("===================================")
    print("")
    
    idInformacao = input("Digite o ID da informação que deseja excluir: ")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # excluir os dados do banco de dados
    cursor.execute(
        "DELETE FROM INFORMACAO WHERE IDINFORMACAO = %s",
        (idInformacao,)
    )
    conn.commit()
    print("Informação complementar excluída com sucesso!")

    # Fechar o cursor e a conexão
    cursor.close()
    conn.close()

    input("Pressione Enter para continuar...")