from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def boas_vindas():
    nome_do_usuario = "Ana"
    
    return render_template('boas_vindas.html', nome=nome_do_usuario)

if __name__ == '__main__':
    app.run(debug=True)