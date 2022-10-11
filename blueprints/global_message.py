from flask import Blueprint, render_template, make_response
from flask_login import current_user, login_required

from forms.global_chat_form import GlobalForm
from flask import Blueprint, render_template, make_response
from flask_login import current_user, login_required

from forms.global_chat_form import GlobalForm
from models.global_message import GlobalMessage
from repository.g_message_repository import GlobalMessageRepository

g_message = Blueprint('global', __name__, url_prefix='/global')

@g_message.get('/')
@login_required
def global_chat_template():
    try:
        g_message_repository = GlobalMessageRepository()
        list = g_message_repository.list()
        
        form = GlobalForm()

        return render_template('global_chat.html', form=form, list=list)
    except Exception as e:
         return make_response(e.__str__(),400)

@g_message.post('/')
@login_required
def global_chat():
    try:
        form = GlobalForm()
        user = current_user
        print(user.username)
        if form.validate_on_submit():
            message = form.message.data
            user_id = user.id

            g_message = GlobalMessage(message, user_id)
            print(g_message.message + g_message.user_id)
            g_message_repository = GlobalMessageRepository()
           
            g_message_repository.add(g_message)
            
        return render_template('global_chat.html', form=form)
        
    except Exception as e:
        return make_response(e.__str__(),400)