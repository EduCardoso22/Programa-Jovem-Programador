from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

produtos = []

@app.route("/")
def home():
    return render_template('produtos.html', teste="teste")

@app.route("/cadastrar", methods=['POST'])
def calcular():
    vNome = request.form['nome']
    vValor = request.form['preco']
    vCategoria = request.form['categoria']

    produtos.append({"nome":vNome, "valor":vValor, "categoria":vCategoria})

    print(produtos)
    return render_template('produtos.html', listaprodutos=produtos)

if __name__ == "__main__":
    app.run(debug=True)
