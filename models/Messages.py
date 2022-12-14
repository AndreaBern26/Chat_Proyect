import uuid

from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base
import models.users
import app

class Message(app.db.Model):
    db = app.db 

    __tablename__ = "messages"

    id = db.Column(db.String(255), primary_key = True)
    message = db.Column(db.String(255))
    message_date = db.Column(db.DATETIME)
    user_to_id = db.Column(db.String(255), db.ForeignKey("users.id"))
    user_from_id = db.Column(db.String(255), db.ForeignKey("users.id"))
    # user_to = relationship("User", foreign_keys = [user_to_id], back_populates = "messages_sent")
    # user_from = relationship("User", foreign_keys = [user_from_id], back_populates = "messages_received")

    def __init__(self, message, user_to, user_from,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.id = str(uuid.uuid4())
        self.message = message
        self.message_date = datetime.now()
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

