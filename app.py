from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseBeta 1.0.2 in main says Hello, Docker!'
