from models.usuario import Usuario

base_usuario = [Usuario(1, 'joao', 'joao@email').to_dict()]

def listar_usuarios():
    return base_usuario

def criar_usuario(nome, email):
    lista_id = [usuario["id"] for usuario in base_usuario]
    if lista_id:
        ultimo_id = max(lista_id)
    else:
        ultimo_id = 0

    usuario = Usuario((ultimo_id + 1), nome, email)
    base_usuario.append(usuario.to_dict())

def buscar_usuario(id):
    resultado = []
    for usuario in base_usuario:
        if int(usuario["id"]) == int(id):
            resultado.append(usuario)
    return resultado

def atualizar_usuario(id, nome, email):
    for usuario in base_usuario:
        if int(usuario['id']) == int(id):
            usuario["nome"] = nome
            usuario["email"] = email

def deletar_usuario(id):
    for indice, usuario in enumerate(base_usuario):
        if int(usuario['id']) == int(id):
            del base_usuario[indice]