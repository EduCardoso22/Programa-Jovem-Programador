# Importação da biblioteca do flask
# jsonify para resposta do servidor
# request capturar as requisições
from flask import Flask, jsonify, request
from flask_cors import CORS

# construindo a aplicação flask
app = Flask(__name__)
CORS(app)


@app.route('/')
def principal():
    return jsonify({"mensagem": "Servidor Funcionando!"})

@app.route('/mensagem')
def mensagem():
    texto = "Este endereço também está funcionando!"
    return jsonify({"mensagem": texto})

@app.route('/pessoa')
def lista():
    lista_pessoas = [{"id": 1, "nome": "João"},{"id": 2, "nome": "Maria"}]
    return jsonify(lista_pessoas)

if __name__ == "__main__":
    # Habilitando o log no console das solicitações
    app.run(debug=True)