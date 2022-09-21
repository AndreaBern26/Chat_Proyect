import uuid

from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

users = []

def get_user(id: str, email: str):
    for user in users:
        if str(user.id) == id or user.email == email:
            return user

    return None

class User(UserMixin):
    def __init__(self, username, email, password, is_admin=False):
        self.id = uuid.uuid4() #Genera una id aleatoria y única.
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
    
    def __repr__(self):
        return self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
