from flask import Blueprint, render_template, make_response
from datetime import datetime

from forms.global_chat_form import GlobalForm
from repository.global_message_repository import GlobalMessageRepository

g_message = Blueprint('global', __name__, url_prefix='/global')

@g_message.get('/')
def global_chat_template():
    form = GlobalForm()
    return render_template('global_chat.html', form = form)

@g_message.post('/')
def global_chat():
    try:
        form = GlobalForm()

        if form.validate_on_submit():
            message = form.message.data
            message_date = datetime.now()
            

        return render_template('global_chat.html', form = form)
        
    except Exception as e:
        return make_response(e.__str__(),400)