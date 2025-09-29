from flask import Blueprint, render_template, request, session, url_for, redirect
from database import listaContas

user_bp = Blueprint('usuarios', __name__, template_folder='../templates')

@user_bp.route("/")
def principal():
    return render_template('index.html')

@user_bp.route("/registro")
def registro():
    return render_template('registro.html')

@user_bp.route("/criar_conta", methods=["POST"])
def criar_conta():
    nome = request.form['nome']
    email = request.form['emailCadastro']
    senha = request.form['senhaCadastro']
    listaContas.append({"nome": nome, "email": email, "senha": senha})
    return render_template('registro.html', mensagem="Conta de acesso criada com sucesso! Clique no link abaixo para realizar o acesso")

@user_bp.route("/login")
def login():
    """ Exibe o formulário de login. """
    return render_template('login.html', contas=listaContas)

@user_bp.route("/logon", methods=["POST"])
def logon():
    email = request.form['emailLogin']
    senha = request.form['senhaLogin']

    for conta in listaContas:
        if conta["email"] == email and conta["senha"] == senha:
            session["login"] = "ok"
            session["nome"] = conta["nome"].capitalize()
            return redirect(url_for('produtos.produtos'))
    
    return render_template('login.html', contas=listaContas, mensagem="Usuário e senha inválidos")

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('usuarios.login'))