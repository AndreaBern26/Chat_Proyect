from models import User

class Admin(User):
    def __init__(self, is_admin=True):
        self.is_admin = is_admin