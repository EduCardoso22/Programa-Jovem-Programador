from flask import Blueprint, jsonify, render_template, request
from services.gasto_service import *
from models.gasto import Gasto

gasto_routes = Blueprint('gasto_routes', __name__)

@gasto_routes.route('/gastos/', methods=["GET"])
def rota_pagina_gastos():
    return render_template("gastos.html")

@gasto_routes.route('/gastos/gastos', methods=["GET"])
def rota_listar_todas_gastos():    
    gastos = gastos_listar_todos()
    return jsonify(gastos)

@gasto_routes.route('/gastos/gasto/<int:id>', methods=["GET"])
def rota_listar_gasto_selecionado(id):
    gasto = gastos_lista_selecionado(id)
    if gasto:
        return jsonify(gasto)
    return jsonify({"mensagem": "Gasto não encontrado"}), 404

@gasto_routes.route('/gastos/gastos/<string:categoria>', methods=["GET"])
def rota_listar_gastos_categoria(categoria):
    gastos = gastos_lista_categoria(categoria)
    return jsonify(gastos)

@gasto_routes.route('/gastos/valor/<string:categoria>', methods=["GET"])
def rota_valor_gastos_categoria(categoria):
    valor_total = gastos_valor_categoria(categoria)
    return jsonify([{"valor": valor_total}])

@gasto_routes.route('/gastos/gasto', methods=["POST"])
def rota_gastos_salvar_novo_gasto():
    dados = request.get_json()
    gasto = Gasto(None, dados.get("descricao"), dados.get("categoria"), dados.get("valor"), dados.get("data_gasto"))
    if gastos_salvar_novo_gasto(gasto):
        return jsonify({"mensagem": "Gasto criado com sucesso"}), 201
    return jsonify({"mensagem": "Erro ao criar o gasto"}), 400
    
@gasto_routes.route('/gastos/gasto/<int:id>', methods=["PUT"])
def rota_gastos_salvar_gasto_existente(id):
    dados = request.get_json()
    gasto = Gasto(id, dados.get("descricao"), dados.get("categoria"), dados.get("valor"), dados.get("data_gasto"))
    if gastos_salvar_gasto_existente(gasto):
        return jsonify({"mensagem": "Gasto alterado com sucesso"})
    return jsonify({"mensagem": "Erro ao alterar o gasto"}), 400

@gasto_routes.route('/gastos/gasto/<int:id>', methods=["DELETE"])
def rota_excluir_gasto_selecionado(id):
    if gastos_excluir_gasto_existente(id):
        return jsonify({"mensagem": "Gasto removido com sucesso"})
    return jsonify({"mensagem": "Erro ao remover o gasto"}), 400