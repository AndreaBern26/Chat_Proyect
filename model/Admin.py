from model import Users

class Admin(Users):
    def __init__(self, is_admin=True):
        self.is_admin = is_admin