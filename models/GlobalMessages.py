import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, DateTime
from models.base import Base
from models.User import User


class GlobalMessage(Base):
    __tablename__ = "global_messages"

    id = Column(String(255), nullable=False, primary_key=True)
    user_id = Column(String(255), ForeignKey("users.id"))
    message = Column(String(255))
    message_date = Column(DateTime)
    user = relationship("User", back_populates="global_messages")


    def __init__(self, user_id, message, message_date):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.message = message
        self.message_date = message_date