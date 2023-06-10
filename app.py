from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='./static', template_folder='./frontend/public')
CORS(app, resources={r"/*":{'origins': "*"}})
@app.route('/register')
def user_reg():
    return render_template('index.html')

@app.route('/test')
def test():
    return "testing"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

