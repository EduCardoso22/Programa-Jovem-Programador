from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

produtos = [
    {"nome": "Batata", "preco": 5.50},
    {"nome": "Queijo", "preco": 7.20},
    {"nome": "Presunto", "preco": 3.40},
    {"nome": "Óleo", "preco": 6.00}
]

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

@app.route("/obtervalor", methods=["POST"])
def obtervalor():
    dados = request.get_json()

    resultado = []
    for produto in produtos:
        for item in dados:
            if item.get("nome") == produto.get("nome"):
                resultado.append(produto)
    
    return jsonify({"itens localizados":resultado})
    
        
if __name__ == "__main__":
    app.run(debug=True)
