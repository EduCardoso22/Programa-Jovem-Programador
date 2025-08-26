from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

dadosRecebidos = []

@app.route("/cadastro", methods=["POST"])
def cadastro():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")

    dadosRecebidos.append({"nome":nome, "email":email})

    return jsonify([{"mensagem":"Dados salvos com sucesso"}])

@app.route("/listar")
def listar():
    return jsonify(dadosRecebidos)

if __name__ == "__main__":
    app.run(debug=True)
