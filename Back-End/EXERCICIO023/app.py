from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def exibir_usuario():
    dados_usuario = {
        'nome': 'Eduardo Cardoso',
        'email': 'eduardo.oliveira20@alunos.sc.senac.br',
        'cidade': 'Florianópolis'
    }
    
    return render_template('usuario.html', usuario=dados_usuario)

if __name__ == '__main__':
    app.run(debug=True)