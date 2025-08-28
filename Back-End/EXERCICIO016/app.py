from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('formulario.html')

        
@app.route("/contato", methods=['POST'])
def receber_contato():
    vNome = request.form['nome']
    vEmail = request.form['email']

    return render_template('mensagem.html', nome=vNome, email=vEmail)

if __name__ == "__main__":
    app.run(debug=True)
