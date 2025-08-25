from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')

def index():
    return jsonify({"message": "Bem-vindo!"})

def media():
    try:
        nota1 = float(request.args.get('nota1'))
        nota2 = float(request.args.get('nota2'))
        nota3 = float(request.args.get('nota3')) 
        resultado = (nota1 + nota2 + nota3) / 3
        return jsonify([{"resultado": f"A média final é {resultado}"}])
    
    except (TypeError, ValueError):
        return jsonify({"error": "Parâmetros inválidos. Certifique-se de passar num1 e num2 como números."})
    
if __name__ == '__main__':
    app.run(debug=True)