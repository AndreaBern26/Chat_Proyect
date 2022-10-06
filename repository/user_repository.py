from models.users import User
import models.users

from repository.abstract_repository import AbstractRepository

class UserRepository(AbstractRepository):
    def get(self, user_id):
        return self.session.query(User).filter_by(id = user_id).one_or_none()
    
    def get_user_by_email(self, email):
        return self.session.query(User).filter_by(email = email).one_or_none()
    
    def list(self):
        return self.session.query(User).all()
    
    def add(self, user: User):
        self.session.add(user)
        self.session.commit()
    
    def connected(self, user, status: bool):
        user.conneted = status
        self.session.commit()
