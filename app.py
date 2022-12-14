import os

from flask import Flask, flash, g, render_template
from flask_wtf import CSRFProtect
from flask_login import LoginManager, current_user, login_required
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder = "templates")
app.config['SECRET_KEY'] = '6d0ad83754dbb3d7c2f5ffc117255906dd3d763b5447b7c9475b3eeccadd348d'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy()
db.init_app(app)
with app.app_context():
    db.create_all()
    
from blueprints.auth import auth
from blueprints.global_message import g_message
from models.global_message import GlobalMessage
from repository.g_message_repository import GlobalMessageRepository
from repository.user_repository import UserRepository

#Blueprints
app.register_blueprint(auth)
app.register_blueprint(g_message)

#SocketIO
socketio = SocketIO(app, manage_session=False, logger=True, engineio_logger=True, cors_allowed_origins="http://127.0.0.1:5000")

@socketio.on('connect')
def user_connect():
    user = current_user
    send(user.username + ' has connected', broadcast=True)

@socketio.on('disconnect')
def user_disconnect():
    user = current_user
    user_repository = UserRepository()
    user_repository.connected(user, False)
    send(user.username + ' has disconnected', broadcast=True)

@socketio.on('message')
def handle_message(msg):
    print ('Message' + msg)
    user = current_user
    g_message = GlobalMessage(message = msg, user_id = user.id)
    g_message_rep = GlobalMessageRepository()
    g_message_rep.add(g_message)

    send(msg, broadcast = True) #True para que le llegue a todos los usuarios.

#Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login_template' #Nombre de la vista de inicio de sesión

@login_manager.user_loader
def load_user(id):
    user_repository = UserRepository()
    user = user_repository.get(id)
    
    if user is not None:
        g.user = user
    return user

@app.get('/')
@login_required
def home():
    user = current_user
    flash('You were sucessfully logged in')
    return render_template('home.html', user=user)

if __name__ == '__main__':
    socketio.run(app)
