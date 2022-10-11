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

from flask import Blueprint, make_response
from flask_login import current_user, login_required

from repository.user_repository import UserRepository

users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

@users.get('/')
@login_required
def get_users():
    user_repository = UserRepository()
    user_list = user_repository.list()
    list_users = [user.to_json('list') for user in user_list]
    
    return make_response(list_users,200)

@users.get('/<id>')
@login_required
def get_user(id):
    try:
        user_repository = UserRepository()
        user = user_repository.get(id)
        return make_response(user, 200)
    except Exception as e:
        return make_response(e.__str__(), 400)

@users.delete('/delete/<user_id>')
@login_required
def delete_user(user_id):
    try:
        user_repository = UserRepository()
        user_del = user_repository.get(user_id)

        if user_del is None:
            raise ValueError(f"The user: {user_id} doesn't exist", 400)
                
        if user_del != current_user.id:
            raise ValueError("Unauthorized", 401)
        
        user_repository.delete(user_del)
        return make_response('user deleted', 200)
    except Exception as e:
        return make_response(e.__str__(), 400)