from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios_cadastrados = {}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario in usuarios_cadastrados:
            mensagem_erro = "Este nome de usuário já está em uso."
            return render_template('cadastro.html', error=mensagem_erro)

        usuarios_cadastrados[usuario] = {'nome': nome, 'senha': senha}
        
        return redirect(url_for('login'))
    
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario]['senha'] == senha:
            nome_do_usuario = usuarios_cadastrados[usuario]['nome']
            mensagem = f"Login feito com sucesso, seja bem vindo {nome_do_usuario}"
        else:
            mensagem = "Credenciais inválidas"
        
        return render_template('login.html', mensagem=mensagem)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)