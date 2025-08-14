from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"mensagem": "Servidor Funcionando! "})

@app.route('/mensagem')
def mensagem():
    motivacional = "Aqueles que não entendem a verdadeira dor nunca vão entender a verdadeira paz."
    return jsonify({"mensagem": motivacional})

if __name__ == "__main__":
    app.run(debug=True)