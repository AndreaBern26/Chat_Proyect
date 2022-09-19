from flask import Flask

app = Flask(__name__)

#Routes
@app.route("/")
def home():
    return "index.html"

app.get('/global')
def getGlobalChat():
    pass

if __name__ == '__main__':
    app.run()