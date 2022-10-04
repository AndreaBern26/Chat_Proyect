from flask import Blueprint, make_response
from flask_login import login_required
from repository.user_repository import UserRepository


users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

@users.get('/')
#@login_required
def get_users():
    user_repository = UserRepository()
    user_list = user_repository.list_all()
    list_users = [user.to_json('list') for user in user_list]

    return make_response(list_users, 200)