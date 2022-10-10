from flask import Blueprint, render_template, make_response, redirect, url_for
from flask_login import current_user, login_user, logout_user

from models.users import User
from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from repository.user_repository import UserRepository

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.get('/login')
def login_template():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    return render_template('auth/login.html', form = form)

@auth.post('/login')
def login():
    try:
        form = LoginForm()

        if form.validate_on_submit():
            user_repository = UserRepository()
            user = user_repository.get_user_by_email(form.email.data)
            
            if user is not None and user.check_password(form.password.data):
                login_user(user, remember = True)
                # try:
                #     user_repository.new_session()
                # except Exception as e:
                #     make_response(e.__str__(), 400)
                user_repository.connected(user, True)
                return redirect(url_for('home'))
        
        return render_template('auth/login.html', form=form)

    except Exception as e:
        return make_response(e.__str__(), 400)

@auth.get('/register')
def register_template():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegisterForm()
    return render_template ('auth/register.html', form = form)

@auth.post('/register')
def register():
    
    try:
        form = RegisterForm()
        
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            
            user = User(username, email, password, is_admin = False)
            user_repository = UserRepository()
            user_repository.add(user)
            
            login_user(user, remember = True)
            user_repository.connected(user, True)
            return redirect(url_for('home'))
            
           
        
        return render_template('auth/register.html', form = form)
    except Exception as e:
        return make_response(e.__str__(),400)

@auth.get('/logout')
def logout():
    logout_user()
    user = current_user
    user_repository = UserRepository()
    user_repository.connected(user, False)

    return redirect(url_for('auth.login_template'))