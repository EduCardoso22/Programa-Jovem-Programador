from flask import Blueprint, jsonify
from database import clientes

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route('/clientes/<int:id>')
def listar_clientes(id):
    for u in clientes:
        if u['id'] == id:
            return jsonify(u)
    return jsonify({"mensagem": "Cliente não encontrado"}), 404