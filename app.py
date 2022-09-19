from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")

@app.get("/login")
def login_template():
    return render_template("login.html")

@app.route('/')
def hello_world():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
