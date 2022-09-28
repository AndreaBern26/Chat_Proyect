import uuid
from xmlrpc.client import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base import Base


class Messages(Base):
    __tablename__ = "messages"
    id = Column(String(255), primary_key=True)
    user_to = Column(String(255), ForeignKey("users.id"))
    user_from = Column(String(255), ForeignKey("users.id"))
    message = Column(String(255))
    message_date = Column(DateTime)
    



    id = uuid.uuid4()

    def __init__(self, user_to, user_from, message, message_date):
        self.user_to = user_to
        self.user_from = user_from
        self.message = message
        self.message_date = message_date