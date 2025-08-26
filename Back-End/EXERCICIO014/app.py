from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

@app.route("/login", methods=["POST"])
def cadastro():
    dados = request.get_json()
    usuario = dados.get("usuario")
    senha = dados.get("senha")

    if (usuario == "admin") and (senha == "123"):
        return jsonify({"mensagem":"Login bem-sucedido"})
    else:
        return jsonify({"mensagem":"Usuário ou senha incorretos"})
        
if __name__ == "__main__":
    app.run(debug=True)
