from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from models.User import users

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField ('Password', validators=[DataRequired()])
    submit = SubmitField ('Sign in')

    def validate_form(self, request):
        username :str = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if len(username) < 2:
            raise ValidationError('Username is too short')
        
        for user in users:
            if user.username == username:
                raise ValidationError('Username already exists')
            
            if user.email == email:
                raise ValidationError('Email is already registered')
        
        if len(password) < 8:
            raise ValidationError('Password is too short')

        return True
