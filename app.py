
from flask import Flask,g, render_template, flash
from flask_login import LoginManager, login_required
from flask_socketio import SocketIO, send

from blueprints.auth import auth
from blueprints.users import users


app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '6d0ad83754dbb3d7c2f5ffc117255906dd3d763b5447b7c9475b3eeccadd348d'

#SocketIO
socketio = SocketIO(app) # Inicializa la conexión del socketIO

@socketio.on('message')
def handle_message(msg):
    print("Message:" + msg)
    send(msg, broadcast = True)






#Blueprints
app.register_blueprint(auth)
app.register_blueprint(users)

#Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login_template' #Nombre de la vista de inicio de sesión

@login_manager.user_loader
def load_user(id):
    for user in user:
        if str(user.id) == id:
            g.user = user
            return user

    g.user = None
    return None

@app.get('/')
def home():
    flash('You were sucessfully logged in')
    return render_template('home.html')

@app.get('/global')
def global_chat():
    return render_template('global_chat.html')

if __name__ == "__main__":
    app.run()
    socketio.run(app)
