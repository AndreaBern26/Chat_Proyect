import uuid

from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin):
    id = uuid.uuid4() #Genera una id aleatoria y única.

    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return self.username

    
