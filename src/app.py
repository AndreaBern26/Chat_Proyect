from flask import Flask, url_for, request, redirect, render_template, make_response
from flask_login import LoginManager, login_user, current_user
from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from models.User import User, getUser, users

app = Flask(__name__, template_folder="templates")

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
