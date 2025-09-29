from flask import Blueprint, jsonify
from services import filme_service

filme_bp = Blueprint('filme_routes', __name__, url_prefix='/api')

@filme_bp.route('/importar', methods=['GET'])
def importar():
    resultado, status_code = filme_service.importar_filmes()
    return jsonify(resultado), status_code

@filme_bp.route('/filmes', methods=['GET'])
def get_filmes():
    return jsonify(filme_service.listar_filmes())