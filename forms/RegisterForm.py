
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length

from models.User import users

def uniqueEmail(form,field):
    for user in users:
        if user['email'] == field.data:
            raise ValidationError('Email already exists')

def uniqueUsername(form,field):
    for user in users:
        if user['username'] == field.data:
            raise ValidationError('Username already exists')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2), uniqueUsername])
    email = StringField('Email', validators=[DataRequired(), Email(), uniqueEmail])
    password = PasswordField ('Password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField ('Sign in')


