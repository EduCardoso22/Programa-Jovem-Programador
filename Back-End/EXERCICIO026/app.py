# app.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'sua-chave-secreta-muito-dificil'

# --- Nosso "Banco de Dados" em memória ---
usuarios = []
produtos = [
    {'id': 1, 'nome': 'Água', 'categoria': 'Bebida', 'valor': 1.99},
    {'id': 2, 'nome': 'Refrigerante', 'categoria': 'Bebida', 'valor': 4.30},
    {'id': 3, 'nome': 'Coxinha', 'categoria': 'Salgado', 'valor': 2.99}
]
# Para garantir que os IDs dos novos produtos sejam únicos
proximo_id_produto = 4

# --- Rotas de Usuário e Autenticação (Já feitas) ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if any(u['email'] == email for u in usuarios):
            flash('Este e-mail já está cadastrado. Tente outro.', 'error')
            return redirect(url_for('registro'))
        novo_usuario = {'nome': nome, 'email': email, 'senha': senha}
        usuarios.append(novo_usuario)
        session['usuario_logado'] = email
        flash('Cadastro realizado e login efetuado com sucesso!', 'success')
        return redirect(url_for('listar_produtos'))
    return render_template('registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario_encontrado = next((u for u in usuarios if u['email'] == email and u['senha'] == senha), None)
        if usuario_encontrado:
            session['usuario_logado'] = email
            flash('Login efetuado com sucesso!', 'success')
            return redirect(url_for('listar_produtos'))
        else:
            flash('E-mail ou senha inválidos. Tente novamente.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario_logado', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('home'))

# --- NOVAS ROTAS DE PRODUTOS (CRUD) ---

@app.route('/produtos')
def listar_produtos():
    if 'usuario_logado' not in session:
        flash('Acesso negado. Por favor, faça login.', 'error')
        return redirect(url_for('login'))
    
    # Agora renderizamos a página de produtos, passando a lista para o template
    return render_template('produtos.html', lista_produtos=produtos)

@app.route('/novoproduto', methods=['GET', 'POST'])
def novoproduto():
    global proximo_id_produto
    if 'usuario_logado' not in session:
        flash('Acesso negado. Por favor, faça login.', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        valor = float(request.form['valor'])
        
        novo_produto = {'id': proximo_id_produto, 'nome': nome, 'categoria': categoria, 'valor': valor}
        produtos.append(novo_produto)
        proximo_id_produto += 1
        
        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_produtos'))
    
    # Para o GET, apenas mostramos o formulário de cadastro
    return render_template('produto_form.html', titulo="Novo Produto")

@app.route('/alterar/<int:id>', methods=['GET', 'POST'])
def alterar_produto(id):
    if 'usuario_logado' not in session:
        flash('Acesso negado. Por favor, faça login.', 'error')
        return redirect(url_for('login'))

    # Encontra o produto a ser alterado
    produto_a_alterar = next((p for p in produtos if p['id'] == id), None)
    if not produto_a_alterar:
        flash('Produto não encontrado.', 'error')
        return redirect(url_for('listar_produtos'))

    if request.method == 'POST':
        produto_a_alterar['nome'] = request.form['nome']
        produto_a_alterar['categoria'] = request.form['categoria']
        produto_a_alterar['valor'] = float(request.form['valor'])
        flash('Produto alterado com sucesso!', 'success')
        return redirect(url_for('listar_produtos'))

    # Para o GET, mostramos o formulário preenchido com os dados do produto
    return render_template('produto_form.html', titulo="Alterar Produto", produto=produto_a_alterar)


@app.route('/excluir', methods=['POST'])
def excluir_produto():
    if 'usuario_logado' not in session:
        flash('Acesso negado. Por favor, faça login.', 'error')
        return redirect(url_for('login'))

    produto_id = int(request.form['produto_id'])
    
    # Remove o produto da lista
    produtos[:] = [p for p in produtos if p['id'] != produto_id]
    
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('listar_produtos'))


if __name__ == '__main__':
    app.run(debug=True, port=5555)