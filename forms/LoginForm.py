from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min = 5), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField('Login')
