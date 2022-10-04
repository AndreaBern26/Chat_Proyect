from repository.abstract_repository import AbstractRepository
from models.messages import Message

class MessageRepository(AbstractRepository):
    def get(self, message_id):
        return self.session.query(Message).filter_by(id = message_id).one_or_none()

    def get_by_user_id(self, user_id):
        return self.session.query(Message).filter_by(user_id = user_id).all()

    def list(self):
        return self.session.query(Message).all()

    def add(self, message):
        self.session.add(message)
        self.session.commit()

    def delete(self, message):
        self.session.delete(message)
        self.session.commit()