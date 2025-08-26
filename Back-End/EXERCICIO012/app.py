from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

dadosRecebidos = []

@app.route("/produto", methods=["POST"])
def cadastro():
    dados = request.get_json()
    nome = dados.get("nome")
    valor = float(dados.get("valor"))
    valor_desconto = round(valor * 0.9, 2)

    dadosRecebidos.append({"nome":nome, "valor":valor, "valor_desconto":valor_desconto})

    return jsonify([{"nome":nome, "valor":valor, "valor_desconto":valor_desconto}])

@app.route("/listar")
def listar():
    return jsonify(dadosRecebidos)

if __name__ == "__main__":
    app.run(debug=True)
