from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def listar_notas():
    lista_de_alunos = [
        {'nome': 'Ana Silva', 'nota': 8.5},
        {'nome': 'João Pereira', 'nota': 5.9},
        {'nome': 'Maria Oliveira', 'nota': 9.2},
        {'nome': 'Pedro Souza', 'nota': 4.3},
        {'nome': 'Carla Martins', 'nota': 7.0},
        {'nome': 'Lucas Costa', 'nota': 6.0}
    ]
    
    return render_template('notas.html', alunos=lista_de_alunos)

if __name__ == '__main__':
    app.run(debug=True)