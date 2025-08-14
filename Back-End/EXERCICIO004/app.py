from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify ({"messagem": "O Servidor está rodando!"})

@app.route('/status')
def status():
    status = [{'status': 'OK', 'versao': '1.0.0', 'autor': 'Eduardo', 'Acesso dia e hora': datetime.now()}]
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)