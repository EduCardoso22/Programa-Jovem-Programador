from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('calculadora.html')

        
@app.route("/calcular", methods=['POST'])
def calcular():
    vNumero1 = int(request.form['numero1'])
    vNumero2 = int(request.form['numero2'])
    vOperacao = request.form['operacao']

    if vOperacao=="+":
        vResultado = vNumero1 + vNumero2
    elif vOperacao=="-":
        vResultado = vNumero1 - vNumero2
    elif vOperacao=="*":
        vResultado = vNumero1 * vNumero2
    elif vOperacao=="/":
        vResultado = vNumero1 / vNumero2
    else:
        vResultado = "operação invalida"

    return render_template('calculadora.html', resultado=vResultado)

if __name__ == "__main__":
    app.run(debug=True)
