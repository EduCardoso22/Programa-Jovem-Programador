from flask import Flask
from flask_cors import CORS
from routes.usuarios import user_bp
from routes.produtos import product_bp

app = Flask(__name__)
CORS(app)

app.secret_key = "senac_123"

app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)