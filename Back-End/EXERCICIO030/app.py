from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from services import filme_service, avaliacao_service

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/filmes')
def pagina_listar_filmes():
    filmes = filme_service.listar_filmes()
    for filme in filmes:
        total = len(avaliacao_service.listar_avaliacoes_por_filme(filme['id']))
        filme['avaliacoes'] = total
    return render_template('filmes.html', filmes=filmes)

@app.route('/avaliacao/<int:filme_id>')
def pagina_avaliacoes(filme_id):
    filme = filme_service.buscar_filme_por_id(filme_id)
    if not filme:
        return "Filme não encontrado!", 404
    
    avaliacoes = avaliacao_service.listar_avaliacoes_por_filme(filme_id)
    return render_template('avaliacoes.html', filme=filme, avaliacoes=avaliacoes)

from routes.filme_routes import filme_bp
from routes.avaliacao_routes import avaliacao_bp

app.register_blueprint(filme_bp)
app.register_blueprint(avaliacao_bp)


if __name__ == '__main__':
    with app.app_context():
        filme_service.importar_filmes()
    app.run(debug=True)