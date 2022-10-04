import uuid

from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.orm import relationship

from models.base import Base
import models.users

class GlobalMessage(Base):
    __tablename__ = 'global_message'

    id = Column(String(255), primary_key = True)
    message = Column (String(255))
    message_date = Column(DATETIME)
    user_id = Column(String(255), ForeignKey('users.id'))
    user = relationship("User", back_populates = "global_messages")

    def __init__(self, message, message_date, user_id):

        self.id = str(uuid.uuid4())
        self.message = message
        self.message_date = message_date
        self.user_id = user_id
