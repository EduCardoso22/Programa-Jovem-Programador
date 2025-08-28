from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

notas = []

@app.route("/")
def home():
    return render_template('notas.html')

@app.route("/cadastrar", methods=['POST'])
def calcular():
    try:
        vNome = request.form['nome']
        vNota1 = float(request.form['nota1'])
        vNota2 = float(request.form['nota2'])
        vNota3 = float(request.form['nota3'])
        vMedia = round((vNota1 + vNota2 + vNota3) / 3, 2)
        vResultado = "Aprovado" if vMedia >= 7 else 'Reprovado'
        vMensagem = "Notas salvas com sucesso e média calculada!"
    except:
        vMensagem = "Erro ao tentar salvar as notas e calcular a média"

    notas.append({"nome":vNome
                  , "nota1":vNota1
                  , "nota2":vNota2
                  , "nota3":vNota3
                  , "media":vMedia
                  , "resultado":vResultado
                })

    return render_template('notas.html', listaNotas=notas, mensagem=vMensagem)

if __name__ == "__main__":
    app.run(debug=True)
