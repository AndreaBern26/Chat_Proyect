from flask import Blueprint, render_template, url_for, make_response, redirect
from flask_login import current_user, login_user, logout_user

from forms.LoginForm import LoginForm
from forms.RegisterForm import RegisterForm
from models.User import User, users, get_user

auth = Blueprint('auth',__name__, url_prefix = '/auth')

@auth.get('/login')
def login_template():
    """
    If the user is correctly authenticated, returns a redirect to home 
    page. If not, the user will stay in the login page.
    
    :return: a redirect or the login template.
    :rtype: path
    """

    if current_user.is_authenticated:
        return redirect( url_for('home'))
    
    form = LoginForm()

    return render_template('templates/auth/login.html', form = form)


@auth.post('/login')

def login():
    """
    Checks if values of login form is correct. If they are correct,
    the user will be redirect to homepage, if not, the user
    will stay in login page and will have to fill the form again.

    :return: a redirect or the login template.
    :rtype: path
    """

    try:
        form = LoginForm()

        if form.validate_on_submit():
            user = get_user(email = form.email.data)

            if user is not None and user.check_password(form.password.data):
                login_user(user, remember = True)
                return redirect( url_for('home'))
        
        return render_template('templates/auth/login.html', form = form)

    except Exception as e:
        return make_response(e.__str__(), 400)

@auth.get('/register')
def register_template():

    """
    If the user is correctly authenticated, returns a redirect to home 
    page. If not, the user will stay in the register page.
    
    :return: a redirect or the register template.
    :rtype: path
    """

    if current_user.is_authenticated:
        return redirect( url_for ('home'))
    
    form = RegisterForm()
    return render_template('templates/auth/register.html', form = form)

@auth.post('/register')
def register():
    """
        Checks the values of register form.
        
        · If values of register form are correct, those values will be saved
            in BBDD creating a new user with them. The user will be logged and
            remembered also.
    
        · If values of register form are incorrect, the users will be stay in
            register template and will have to fill the form again.
    
    """

    try:
        form = RegisterForm()

        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            user = User (username, email, password)
            users.append(user)

            login_user(user, remember = True) #Recuérdame activado.

            return redirect('home')
        
        return render_template('templates/auth/registro.html', form = form)

    except Exception as e:
        return make_response(e.__str__(),400)


@auth.get('/logout')
def logout():
    """
    Allows users to log out from their account

    :return: a redirect to login form.
    :rtype: path
    """
    logout_user()
    return redirect(url_for('login_template'))
