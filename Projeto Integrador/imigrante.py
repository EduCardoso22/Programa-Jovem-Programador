from conn import Conectar


def NovoImigrante():
    print("=======================")
    print("Cadastro de Imigrante")
    print("=======================")
    print("")

    nome = input("Digite o nome do imigrante: ")
    nacionalidade = input("Digite a nacionalidade do imigrante: ")
    dataNascimento = input("Digite a data de nascimento do imigrante (AAAA-MM-DD): ")
    documento = input("Digite o número do documento do imigrante: ")

    # criando conexão

    conn = Conectar()
    cursor = conn.cursor()
    # enviar os dados para o banco de dados
    cursor.execute(
        "INSERT INTO IMIGRANTE (NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO) VALUES (%s, %s, %s, %s)",
        (nome, nacionalidade, dataNascimento, documento)
    )
    conn.commit()  # Salvar as alterações no banco de dados
    print("")
    print("Imigrante cadastrado com sucesso!")

    input("Pressione Enter para continuar...")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def ListarImigrantes():
    print("=======================")
    print("Listagem de Imigrantes")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()
    # consultar os dados no banco de dados

    cursor.execute(
        "SELECT NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE"
    )
    for nome, nacionalidade, dataNascimento, documento in cursor.fetchall():
        print(
            f" Nome: {nome}, Nacionalidade: {nacionalidade}, Data de Nascimento: {dataNascimento}, Documento: {documento}"
        )
    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados


def DetalheImigrante(id):
    print("=======================")
    print("Detalhe do Imigrante")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # consultar os dados no banco de dados
    cursor.execute(
        "SELECT IDIMIGRANTE, NOME, NACIONALIDADE, DT_NASCIMENTO, DOCUMENTO FROM IMIGRANTE WHERE IDIMIGRANTE = %s",
        (id,)
    )

    for id, nome, nacionalidade, dataNascimento, documento in cursor.fetchall():
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" Nacionalidade: {nacionalidade}")
        print(f" Data de Nascimento: {dataNascimento}")
        print(f" Documento: {documento}")

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dadoss

def AlterarImigrante(id):
    print("=======================")
    print("Alteração de Imigrante")
    print("=======================")
    print("")

    print("Digite os novos dados do imigrante:")
    nome = input("Digite o nome do imigrante: ")
    nacionalidade = input("Digite a nacionalidade do imigrante: ")
    dataNascimento = input("Digite a data de nascimento do imigrante (AAAA-MM-DD): ")
    documento = input("Digite o número do documento do imigrante: ")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()

    # enviar os dados para o banco de dados
    cursor.execute(
        "UPDATE IMIGRANTE SET NOME = %s, NACIONALIDADE = %s, DT_NASCIMENTO = %s, DOCUMENTO = %s WHERE IDIMIGRANTE = %s",
        (nome, nacionalidade, dataNascimento, documento, id)
    )
    conn.commit()  # Salvar as alterações no banco de dados

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados

    print("Alteração realizada com sucesso!")
    input("Pressione Enter para voltar ao menu...")


def DeletaImigrante(id):
    print("=======================")
    print("Deletar Imigrante")
    print("=======================")
    print("")

    # criando conexão
    conn = Conectar()
    cursor = conn.cursor()
    # enviar os dados para o banco de dados
    cursor.execute(
        "DELETE FROM IMIGRANTE WHERE IDIMIGRANTE = %s",
        (id,)
    )
    conn.commit()  # Salvar as alterações no banco de dados

    # fechar a conexão
    cursor.close()  # Fechar o cursor
    conn.close()  # Fechar a conexão com o banco de dados

    print("Imigrante deletado com sucesso!")
    input("Pressione Enter para voltar ao menu...")
