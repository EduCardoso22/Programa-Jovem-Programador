from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify([{"mensagem": "Backend funcionando"}])

@app.route('/boasvindas')
def mensagem():
    nome = request.args.get('nome')
    return jsonify([{"mensagem": f"Seja bem vindo {nome.capitalize()}"}])

if __name__ == '__main__':
    app.run(debug=True)