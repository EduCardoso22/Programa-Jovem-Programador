from flask import Blueprint, jsonify
from database import produtos

produto_bp = Blueprint('produtos', __name__)

@produto_bp.route('/produtos/<int:id>')
def listar_produtos(id):
    for p in produtos:
        if p['id'] == id:
            return jsonify(p)
    return jsonify({"mensagem": "Produto não encontrado"}), 404