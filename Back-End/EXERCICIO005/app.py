from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def principal():
    return jsonify({"menssagem": "Este programa está funcionando!"})

if __name__ == '__main__':
    app.run(debug=True)