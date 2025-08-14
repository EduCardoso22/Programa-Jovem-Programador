from flask import Flask, jsonify, Request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/produto')
def produtos():
    lista_produtos = [{"id": 1, "nome": "Mamão", "preco": 10.0},{"id": 2, "nome": "Maçã", "preco": 07.0}]
    return jsonify(lista_produtos)

if __name__ == "__main__":
    app.run(debug=True)