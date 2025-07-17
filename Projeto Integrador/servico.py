from conn import Conectar


def NovoServico():

    print("=======================")
    print("Cadastro de Serviço")
    print("=======================")
    print("")

    tipo = input("Digite o tipo de serviço (ex: ONG, Acolhimento, Jurídico, etc.): ")
    nome = input("Digite o nome do serviço: ")
    endereco = input("Digite a endereço do serviço: ")
    telefone = input("Digite o telefone do serviço: ")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # inserir os dados no banco de dados
    cursor.execute(
        "INSERT INTO SERVICO_APOIO (TIPO, NOME, ENDERECO, TELEFONE) VALUES (%s, %s, %s, %s)",
        (tipo, nome, endereco, telefone),
    )

    conn.commit()  # Confirmar a transação

    print("")
    print("Serviço cadastrado com sucesso!")

    input("Pressione Enter para continuar...")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def ListarServicos():
    print("=======================")
    print("Listagem de Serviços")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # consultar os dados no banco de dados
    cursor.execute("SELECT TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO")

    for tipo, nome, endereco, telefone in cursor.fetchall():
        print(f"Tipo: {tipo}, Nome: {nome}, Endereço: {endereco}, Telefone: {telefone}")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def DetalheServico(id):
    print("=======================")
    print("Detalhe do Serviço")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # consultar os dados no banco de dados
    cursor.execute(
        "SELECT IDSERVICO_APOIO, TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO WHERE IDSERVICO_APOIO = %s",
        (id,),
    )

    servico = cursor.fetchone()

    if servico:
        id_servico, tipo, nome, endereco, telefone = servico
        print(
            f"ID: {id_servico}, Tipo: {tipo}, Nome: {nome}, Endereço: {endereco}, Telefone: {telefone}"
        )
    else:
        print("Serviço não encontrado.")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def AlterarServico(id):
    print("=======================")
    print("Alteração de Serviço")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # consultar os dados no banco de dados
    cursor.execute(
        "SELECT TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO WHERE IDSERVICO_APOIO = %s",
        (id,),
    )

    servico = cursor.fetchone()

    if servico:
        tipo, nome, endereco, telefone = servico
        print(f"Tipo: {tipo}, Nome: {nome}, Endereço: {endereco}, Telefone: {telefone}")

        novo_tipo = (
            input("Digite o novo tipo de serviço (deixe em branco para não alterar): ")
            or tipo
        )
        novo_nome = (
            input("Digite o novo nome do serviço (deixe em branco para não alterar): ")
            or nome
        )
        novo_endereco = (
            input(
                "Digite o novo endereço do serviço (deixe em branco para não alterar): "
            )
            or endereco
        )
        novo_telefone = (
            input(
                "Digite o novo telefone do serviço (deixe em branco para não alterar): "
            )
            or telefone
        )

        # atualizar os dados no banco de dados
        cursor.execute(
            "UPDATE SERVICO_APOIO SET TIPO = %s, NOME = %s, ENDERECO = %s, TELEFONE = %s WHERE IDSERVICO_APOIO = %s",
            (novo_tipo, novo_nome, novo_endereco, novo_telefone, id),
        )

        conn.commit()  # Confirmar a transação

        print("")
        print("Serviço alterado com sucesso!")
    else:
        print("Serviço não encontrado.")

    input("Pressione Enter para continuar...")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def DeletaServico(id):
    print("=======================")
    print("Deletar Serviço")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # consultar os dados no banco de dados
    cursor.execute("DELETE FROM SERVICO_APOIO WHERE IDSERVICO_APOIO = %s", (id,))
    conn.commit()

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados

    print("Serviço deletado com sucesso!")
    input("Pressione Enter para continuar...")


def BuscarServicoPorTipo(tipo):
    print("=======================")
    print(f"Serviços do tipo: {tipo}")
    print("=======================")
    print("")
    tipo = input("Informe o tipo de servico (uma parte do texto): ")

    # criando a conexao
    conn = Conectar()
    cursor = conn.cursor()

    # enviando o camando para o banco de dados
    cursor.execute(
        f"SELECT IDSERVICO_APOIO, TIPO, NOME, ENDERECO, TELEFONE FROM SERVICO_APOIO WHERE UPPER(TIPO) LIKE UPPER('%{tipo}%')"
    )

    # percorrendo o resultado e mostrando em tela
    for id, tipo, nome, endereco, telefone in cursor.fetchall():
        print(f"{id} - {tipo} - {nome} - {endereco} - {telefone}")

    # fechando a conexao
    cursor.close()
    conn.close()
