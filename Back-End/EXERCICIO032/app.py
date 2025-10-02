from flask import Flask, jsonify
from flask_cors import CORS

from routes.gasto_routes import gasto_routes

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    rotas = [str(r) for r in app.url_map.iter_rules()]
    return jsonify({
        "mensagem": "Servidor de controle de gastos está no ar!",
        "rotas_disponiveis": rotas
    })

app.register_blueprint(gasto_routes)

if __name__ == "__main__":
    app.run(debug=True)