# Importação da biblioteca do flask
# jsonify para resposta do servidor
# request capturar as requisições
from flask import Flask, jsonify, request
from flask_cors import CORS

# construindo a aplicação flask
app = Flask(__name__)
CORS(app)

