from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
from models.User import users

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(min = 5)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField('Login')

    def validate_form(self,request):
        email = request.form.get('email')
        password = request.form.get('password')

        for user in users:
            if user.email != email:
                raise ValidationError('Email doesn\'t exists')
            
            if user.password != password:
                raise ValidationError('Incorrect password')

        return True