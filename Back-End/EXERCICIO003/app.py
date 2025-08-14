from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [{"id": 1, "nome": "João", "email": "joao@gmail.com", "cidade": "São Paulo"},
           {"id": 2, "nome": "Maria", "email": "maria@hotmail.com", "cidade": "Rio de Janeiro"},
           {"id": 3, "nome": "Pedro", "email": "pedro@outlook.com", "cidade": "Belo Horizonte"},
           {"id": 4, "nome": "Ana", "email": "ana@yahoo.com", "cidade": "Curitiba"}]

@app.route('/')
def principal():
    return jsonify({"Lista de usuários": usuarios})

@app.route('/usuario')
@app.route('/usuario/<int:id>')
def detalhe(id=0):
    resultado = {}
    for usuario in usuarios:
        if usuario['id'] == id:
            resultado = usuario
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)