from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/soma', methods=['GET'])
def soma():
    try:
        numero1 = int(request.args.get('num1'))
        numero2 = int(request.args.get('num2'))
        
        resultado = numero1 + numero2
        return jsonify([{"resultado": f"A soma de {numero1} e {numero2} é {resultado}"}])
    
    except (TypeError, ValueError):
        return jsonify({"error": "Parâmetros inválidos. Certifique-se de passar num1 e num2 como inteiros."})
    
if __name__ == '__main__':
    app.run(debug=True)