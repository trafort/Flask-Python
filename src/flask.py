from flask import Flask
app = Flask(__test__)

@app.route("/")
def hello():
    return "Hello World!"
