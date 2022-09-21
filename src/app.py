from flask import Flask, render_template
from blueprints import user


app = Flask(__name__, template_folder="templates")
app.register_blueprint(user)


@app.route('/')
def home():
    return "Hello world!"

app.get('/global')
def getGlobalChat():
    pass

@app.get("/login")
def login_template():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()