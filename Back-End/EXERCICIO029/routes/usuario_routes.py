from flask import Blueprint, jsonify, render_template, request
from services.usuario_service import *

usuario_routes = Blueprint('usuario_routes', __name__)

@usuario_routes.route('/usuarios')
def home_usuario():
    return render_template('usuario.html')

@usuario_routes.route('/usuario/usuarios', methods=["GET"])
def listar_todos_usuario():    
    usuarios = listar_usuarios()
    return jsonify(usuarios)

@usuario_routes.route('/usuario/usuario', methods=["POST"])
def salvar_usuario():   
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    usuarios = criar_usuario(nome, email)
    return jsonify([{"Mensagem":"Usuario criado com sucesso"}])

@usuario_routes.route('/usuario/usuario', methods=["PUT"])
def alterar_usuario():   
    dados = request.get_json()
    id = dados.get("id")
    nome = dados.get("nome")
    email = dados.get("email")
    usuarios = atualizar_usuario(id, nome, email)
    return jsonify([{"Mensagem":"Usuario alterado com sucesso"}])


@usuario_routes.route('/usuario/usuario/<int:id>')
def detalhe_usuario(id):
    usuario = buscar_usuario(id)
    return jsonify(usuario)

@usuario_routes.route('/usuario/usuario/<int:id>', methods=["DELETE"])
def remover_usuario(id):
    deletar_usuario(id)
    return jsonify([{"Mensagem":"Usuario removido com sucesso"}])