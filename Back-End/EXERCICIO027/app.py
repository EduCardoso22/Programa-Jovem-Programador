from flask import Flask
from routes.clientes import cliente_bp
from routes.produtos import produto_bp

app = Flask(__name__)

@app.route('/')
def home():
    return "API de Clientes e Produtos"

app.register_blueprint(cliente_bp)
app.register_blueprint(produto_bp)

if __name__ == '__main__':
    app.run(debug=True)