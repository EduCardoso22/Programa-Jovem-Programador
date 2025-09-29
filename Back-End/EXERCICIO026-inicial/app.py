from flask import Flask, jsonify, request, render_template, url_for, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "senac_123"
CORS(app)

listaContas = []
listaProdutos = []
listaCategoria = ["Bebida", "Salgado", "Doce"]
ultimoID_produto = 0

@app.route("/")
def principal():
    return render_template('index.html')

@app.route("/registro")
def registro():
    return render_template('registro.html')

@app.route("/criar_conta", methods=["POST"])
def criar_conta():
    nome = request.form['nome']
    email = request.form['emailCadastro']
    senha = request.form['senhaCadastro']
    listaContas.append({"nome":nome, "email":email, "senha":senha})
    return render_template('registro.html', mensagem="Contra de acesso criada com sucesso! Clique no link abaixo para realizar o acesso")

@app.route("/login")
def login():
    return render_template('login.html', contas=listaContas)

@app.route("/logon", methods=["POST"])
def logon():
    email = request.form['emailLogin']
    senha = request.form['senhaLogin']

    flag = False
    for conta in listaContas:
        if(conta["email"] == email and conta["senha"] == senha):
            flag = True
            session["login"] = "ok"
            session["nome"] = conta["nome"].capitalize()
    if flag:
        return produtos()
    else:
        return render_template('login.html', contas=listaContas, mensagem="Usuário e senha inválidos")

@app.route("/logout")
def logout():
    session.clear()
    return login()

@app.route("/produtos")
def produtos():
    if session.get("login") == "ok":
        return render_template('produtos.html', rota_destino="/cadastrar", produtos=listaProdutos)
    else:
        return render_template('index.html', contas=listaContas, mensagem="Faça login para acessar a pagina de produtos")

@app.route("/produto/novo")
def novo():
    return render_template('novo.html', categorias=listaCategoria)

@app.route("/produto/excluir/<int:id>")
def excluir(id):
    for i, produto in enumerate(listaProdutos):
        if produto["id"] == id:
            del listaProdutos[i]
            break   
    return produtos()

@app.route("/produto/editar/<int:id>")
def editar(id):
    for i, produto in enumerate(listaProdutos):
        if produto["id"] == id:
            produto = listaProdutos[i]
            break   
    if produto:
        return render_template('editar.html', categorias=listaCategoria, produto=produto)
    else:
        return produtos()

@app.route("/produto/salvar", methods=["POST"])
def salvar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']
    global ultimoID_produto
    ultimoID_produto += 1
    listaProdutos.append({"id":ultimoID_produto, "nome":nome, "categoria":categoria, "preco":preco})
    return produtos()

@app.route("/produto/alterar", methods=["POST"])
def alterar():
    id = int(request.form['id'])
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']

    for i, produto in enumerate(listaProdutos):
        if produto["id"] == id:
            listaProdutos[i]["nome"] =  nome
            listaProdutos[i]["categoria"] =  categoria
            listaProdutos[i]["preco"] =  preco
            break 
    return produtos()

if __name__ == "__main__":
    app.run(debug=True)
