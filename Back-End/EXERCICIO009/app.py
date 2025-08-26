from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify([{"mensagem":"Backend funcionando"}])

@app.route("/dobro/<int:numero>")
def dobro(numero):
    return jsonify([{"mensagem":f"O dobro de {numero} é {numero * 2}"}])

if __name__ == "__main__":
    app.run(debug=True)
