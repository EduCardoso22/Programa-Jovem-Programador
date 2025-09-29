from flask import Blueprint, render_template, request, session, redirect, url_for
import database

product_bp = Blueprint('produtos', __name__, template_folder='../templates')

@product_bp.route("/produtos")
def produtos():
    if session.get("login") == "ok":
        return render_template('produtos.html', produtos=database.listaProdutos)
    else:
        return redirect(url_for('usuarios.login', mensagem="Faça login para acessar a página de produtos"))

@product_bp.route("/produto/novo")
def novo():
    if session.get("login") != "ok":
        return redirect(url_for('usuarios.login'))
    return render_template('novo.html', categorias=database.listaCategoria)

@product_bp.route("/produto/excluir/<int:id>")
def excluir(id):
    if session.get("login") != "ok":
        return redirect(url_for('usuarios.login'))
        
    for i, produto in enumerate(database.listaProdutos):
        if produto["id"] == id:
            del database.listaProdutos[i]
            break
    return redirect(url_for('produtos.produtos'))

@product_bp.route("/produto/editar/<int:id>")
def editar(id):
    if session.get("login") != "ok":
        return redirect(url_for('usuarios.login'))
        
    produto_encontrado = None
    for produto in database.listaProdutos:
        if produto["id"] == id:
            produto_encontrado = produto
            break
            
    if produto_encontrado:
        return render_template('editar.html', categorias=database.listaCategoria, produto=produto_encontrado)
    else:
        return redirect(url_for('produtos.produtos'))

@product_bp.route("/produto/salvar", methods=["POST"])
def salvar():
    if session.get("login") != "ok":
        return redirect(url_for('usuarios.login'))
        
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']
    
    database.ultimoID_produto += 1
    
    database.listaProdutos.append({"id": database.ultimoID_produto, "nome": nome, "categoria": categoria, "preco": preco})
    return redirect(url_for('produtos.produtos'))

@product_bp.route("/produto/alterar", methods=["POST"])
def alterar():
    if session.get("login") != "ok":
        return redirect(url_for('usuarios.login'))
        
    id = int(request.form['id'])
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']

    for i, produto in enumerate(database.listaProdutos):
        if produto["id"] == id:
            database.listaProdutos[i]["nome"] = nome
            database.listaProdutos[i]["categoria"] = categoria
            database.listaProdutos[i]["preco"] = preco
            break
            
    return redirect(url_for('produtos.produtos'))