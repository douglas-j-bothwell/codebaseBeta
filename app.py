from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseBeta 2.0.4 in my-feature-branch says Hello, Docker!'
