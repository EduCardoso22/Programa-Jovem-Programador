from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def listar_funcionarios():
    lista_de_funcionarios = [
        {'nome': 'Ana', 'foto': 'ana.jpg'},
        {'nome': 'João', 'foto': 'joao.jpg'},
        {'nome': 'Maria', 'foto': 'maria.jpg'}
    ]
    
    return render_template('funcionarios.html', funcionarios=lista_de_funcionarios)

if __name__ == '__main__':
    app.run(debug=True)