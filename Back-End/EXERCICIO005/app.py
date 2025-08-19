from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

alunos = [{'id': 1, 'nome': 'João', 'disciplina': [{'nome': 'Matemática', 'AV1': '8', 'AV2': '9'}, {'nome': 'Geografia', 'AV1': '7', 'AV2': '8'}, {'nome': 'Ciências', 'AV1': '8', 'AV2': '9'}]},
{'id': 2, 'nome': 'Maria', 'disciplina': [{'nome': 'Matemática', 'AV1': '7', 'AV2': '8'}, {'nome': 'Geografia', 'AV1': '9', 'AV2': '10'}, {'nome': 'Ciências', 'AV1': '6', 'AV2': '7'}]},
{'id': 3, 'nome': 'Pedro', 'disciplina': [{'nome': 'Matemática', 'AV1': '10', 'AV2': '9'}, {'nome': 'Geografia', 'AV1': '8', 'AV2': '7'}, {'nome': 'Ciências', 'AV1': '9', 'AV2': '10'}]},
{'id': 4, 'nome': 'Ana', 'disciplina': [{'nome': 'Matemática', 'AV1': '6', 'AV2': '7'}, {'nome': 'Geografia', 'AV1': '8', 'AV2': '9'}, {'nome': 'Ciências', 'AV1': '7', 'AV2': '8'}]}
]

@app.route('/')
def principal():
    return jsonify({"menssagem": "Este programa está funcionando! Seja bem-vindo!"})

@app.route('/alunos')
def listar_alunos():
    return jsonify(alunos)

@app.route('/aluno/<int:id>')
def obter_aluno(id=0):
    resultado = {}
    for aluno in alunos:
        if aluno['id'] == id:
            resultado = aluno
    
    return jsonify(resultado)

@app.route('/notas')
def listar_notas():
    notas = []
    for aluno in alunos:
        notas.append({
            'nome': aluno['nome'],
            'notas': {disciplina['nome']: {'AV1': disciplina['AV1'], 'AV2': disciplina['AV2']} for disciplina in aluno['disciplina']}
        })
    return jsonify(notas)

@app.route('/aluno/<id>/<disciplina>')
def obter_notas_aluno(id, disciplina):
    resultado = {}
    for aluno in alunos:
        if aluno['id'] == int(id):
            for d in aluno['disciplina']:
                if d['nome'].lower() == disciplina.lower():
                    resultado = {
                        'nome': aluno['nome'],
                        'disciplina': d['nome'],
                        'AV1': d['AV1'],
                        'AV2': d['AV2']
                    }
                    break
            break
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)