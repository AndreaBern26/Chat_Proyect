from models.users import User

class Admin(User):
    def __init__(self, username, email, password, is_admin=True):
        super().__init__(username, email, password)
        self.is_admin = is_admin