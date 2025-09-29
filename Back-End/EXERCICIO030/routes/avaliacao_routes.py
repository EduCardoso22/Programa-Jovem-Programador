from flask import Blueprint, request, jsonify, redirect, url_for
from services import avaliacao_service
from services import filme_service

avaliacao_bp = Blueprint('avaliacao_routes', __name__, url_prefix='/api')

@avaliacao_bp.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    return jsonify(avaliacao_service.listar_todas_avaliacoes())

@avaliacao_bp.route('/avaliacoes/total', methods=['GET'])
def get_total_avaliacoes():
    return jsonify(avaliacao_service.total_avaliacoes())

@avaliacao_bp.route('/avaliacao/<int:id>', methods=['GET'])
def get_avaliacao(id):
    avaliacao = avaliacao_service.buscar_avaliacao_por_id(id)
    if avaliacao:
        return jsonify(avaliacao)
    return jsonify({"erro": "Avaliação não encontrada."}), 404

@avaliacao_bp.route('/avaliacao', methods=['POST'])
def post_avaliacao():
    dados = request.form

    try:
        filme_id = int(dados.get('filme_id'))
    except (ValueError, TypeError):
        return jsonify({"erro": "ID de filme inválido."}), 400

    if not filme_service.buscar_filme_por_id(filme_id):
        return jsonify({"erro": f"Filme com ID {filme_id} não encontrado na lista local."}), 404
    
    nova_avaliacao, mensagem = avaliacao_service.criar_avaliacao(dados)
    
    if not nova_avaliacao:
        return jsonify({"erro": mensagem}), 400
        
    return redirect(url_for('pagina_avaliacoes', filme_id=filme_id))


@avaliacao_bp.route('/avaliacao/<int:id>', methods=['PUT'])
def put_avaliacao(id):
    dados = request.json
    avaliacao_atualizada, mensagem = avaliacao_service.atualizar_avaliacao(id, dados)
    if avaliacao_atualizada:
        return jsonify({"mensagem": mensagem, "avaliacao": avaliacao_atualizada})
    return jsonify({"erro": mensagem}), 404

@avaliacao_bp.route('/avaliacao/<int:id>', methods=['DELETE'])
def delete_avaliacao(id):
    sucesso, mensagem = avaliacao_service.excluir_avaliacao(id)
    if sucesso:
        return jsonify({"mensagem": mensagem})
    return jsonify({"erro": mensagem}), 404