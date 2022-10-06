from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError, Length

from repository.user_repository import UserRepository

def unique_email(form,field):
    user_repository = UserRepository()
    user = user_repository.get_user_by_email(field.data)
    if user is not None:
        raise ValidationError('Email already exists')

def unique_username(form,field):
    user_repository = UserRepository()
    user = user_repository.get_user_by_username(field.data)
    if user is not None:
        raise ValidationError('Username already exists')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 2), unique_username])
    email = StringField('Email', validators=[DataRequired(), Email(), unique_email])
    password = PasswordField ('Password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField ('Sign in')


