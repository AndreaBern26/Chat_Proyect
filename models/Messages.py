import uuid

from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.orm import relationship

from models.base import Base
import models.users

class Message(Base):
    __tablename__ = "messages"

    id = Column(String(255), primary_key = True)
    message = Column(String(255))
    message_date = Column(DATETIME)
    user_to = Column(String(255), ForeignKey("users.id"))
    user_from = Column(String(255), ForeignKey("users.id"))
    user = relationship("User", back_populates = "messages")

    def __init__(self,message, message_date, user_to, user_from):
        self.id = str(uuid.uuid4())
        self.message = message
        self.message_date = message_date
        self.user_to = user_to
        self.user_from = user_from
    
    def to_json(self, type: str = 'show'):
        if type == 'list':
            return {
                'id': self.id,
                'message': self.message,
                'message_date': self.message_date
            }

        elif type == 'show':
            return {
                'id': self.id,
                'message': self.message,
                'message_date': self.message_date,
                'user_from': self.user_from,
                'user_to': self.user_to
            }
