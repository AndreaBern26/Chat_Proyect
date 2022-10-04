from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class GlobalForm(FlaskForm):
    message = StringField('Message')
    submit = SubmitField('Send')