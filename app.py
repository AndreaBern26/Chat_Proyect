from flask import Flask

app = Flask(__name__)

#Routes
@app.route("/")
def home():
    return "index.html"

