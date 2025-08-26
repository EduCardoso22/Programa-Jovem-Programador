from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

@app.route("/notas", methods=["POST"])
def cadastro():
    dados = request.get_json()
    nota1 = float(dados.get("nota1"))
    nota2 = float(dados.get("nota2"))
    nota3 = float(dados.get("nota3"))
    media = round((nota1 + nota2 + nota3) / 3, 2)
    
    resultado = "aprovado" if media >= 7 else "Reprovado"

    dados["media"] = media
    dados["resultado"] = resultado

    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)
