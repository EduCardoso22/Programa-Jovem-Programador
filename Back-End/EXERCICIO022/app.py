from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def listar_produtos():
    lista_de_produtos = [
        {'nome': 'Notebook Gamer', 'preco': 5450.99},
        {'nome': 'Monitor 4K 27"', 'preco': 1899.00},
        {'nome': 'Teclado Mecânico RGB', 'preco': 350.50},
        {'nome': 'Mouse Sem Fio', 'preco': 120.00},
        {'nome': 'Headset 7.1', 'preco': 499.90},
        {'nome': 'Cadeira Gamer', 'preco': 1250.00}
    ]
    
    return render_template('produtos.html', produtos=lista_de_produtos)

if __name__ == '__main__':
    app.run(debug=True)