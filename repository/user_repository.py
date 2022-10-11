from models.users import User
import models.users
import app

class UserRepository():
    session = app.db.session

    def get(self, user_id):
        return self.session.query(User).filter_by(id=user_id).one_or_none()
    
    def get_user_by_email(self, email):
        return self.session.query(User).filter_by(email=email).one_or_none()
    
    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(username=username).one_or_none()
    
    def list(self):
        return self.session.query(User).all()
    
    def add(self, user: User):
        self.session.add(user)
        self.session.commit()
    
    def connected(self, user, status: bool):
        user.conneted = status
        self.session.commit()

    