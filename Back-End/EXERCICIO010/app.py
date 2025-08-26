from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

@app.route("/aluno/<nome>/<int:idade>")
def dobro(nome, idade):
    resultado = {"nome":nome, "idade":idade}
    return jsonify([resultado])

if __name__ == "__main__":
    app.run(debug=True)
