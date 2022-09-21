from flask_login import UserMixin

users = []

class Users(UserMixin):
    def __init__(self, id, username, email, password, is_admin=False):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
    
    def __repr__(self):
        return self.username
