import uuid
from xmlrpc.client import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from models.base import Base


class GlobalMessage(Base):
    __tablename__ = "global_messages"

    id = Column(String(255), nullable=False, primary_key=True)
    user_id = Column(String(255), ForeignKey("users.id"))
    message = Column(String(255))
    message_date = Column(DateTime)

    id = uuid.uuid4()

    def __init__(self, user_id, message, message_date):
        self.user_id = user_id
        self.message = message
        self.message_date = message_date