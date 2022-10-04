from flask import Blueprint, make_response, redirect, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename
from forms import CreateForm

from models.users import User
from repository.admin_repository import AdminRepository



admin = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')

@admin.get('/users')
#@login_required
def get_users():
    admin_repository = AdminRepository()
    user_list = admin_repository.list_all()
    list_users = [user.to_json('list') for user in user_list]

    return make_response(list_users, 200)

@admin.get('/users/<id>')
#@login_required
def get_user_by_id(id):
    admin_repository = AdminRepository()
    user_list = admin_repository.find_user_by_id()
    list_users = [user.to_json('list') for user in user_list]

    return make_response(list_users, 200)

@admin.post("/users/add")
#@login_required
def add_user():

    form = CreateForm()

    if form.validate_on_submit():
            username = form.title.data
            email = form.email.data
            password = form.password.data
    new_user = User(username, email, password)
    admin_repository = AdminRepository()
    user_new = admin_repository.createUser(new_user)
    return redirect(url_for('create-user.show', user_new=new_user))
    #return make_response(user_new, 200)