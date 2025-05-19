from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Primeira aplicação no Git!"



if __name__ == '__main__':
    app.run(debug=True)