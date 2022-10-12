from flask import Blueprint, render_template, make_response
from flask_login import current_user, login_required

from models.global_message import GlobalMessage
from repository.g_message_repository import GlobalMessageRepository

g_message = Blueprint('global',__name__, url_prefix='/global')

@g_message.get('/')
@login_required
def global_chat_template():
    try:
        g_message_repository = GlobalMessageRepository()
        list = g_message_repository.list()

        return render_template('global_chat.html', list=list)
    except Exception as e:
         return make_response(e.__str__(),400)

@g_message.delete('/delete/<g_message_id>')
@login_required
def delete_g_message(g_message_id):
    try:
        g_message_repository = GlobalMessageRepository()
        g_message = g_message_repository.get(g_message_id)
        
        if g_message is None:
            raise ValueError("The message doesn't exist")

        if g_message.user_id != current_user.id:
            raise ValueError("Unauthorized", 401)
        
        g_message_repository.delete(g_message)

        return make_response('Message deleted', 200)
    
    except Exception as e:
        return make_response(e.__str__(), 400)