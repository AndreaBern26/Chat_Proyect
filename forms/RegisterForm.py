from collections import UserList
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError,Length
from models.User import users

def uniqueEmail(form,field):
    for user in UserList:
        if user['email'] == field.data:
            raise ValidationError('Email already exists')

def uniqueUsername(form,field):
    for user in UserList:
        if user['username'] == field.data:
            raise ValidationError('Username already exists')


class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2), uniqueUsername])
    email = StringField('Email', validators=[DataRequired(), Length(min = 5), uniqueEmail])
    password = PasswordField ('Password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField ('Sign in')


