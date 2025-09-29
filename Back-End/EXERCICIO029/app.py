from flask import Flask, jsonify
from flask_cors import CORS

from routes.usuario_routes import usuario_routes

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"mensagem":"Backend funcionando!"})

app.register_blueprint(usuario_routes)

if __name__ == "__main__":
    app.run(debug=True)