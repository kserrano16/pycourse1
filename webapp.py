#pip install flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola amigos de Geeky Theory'

if __name__=='__main__':
    app.run(host='0.0.0.0')