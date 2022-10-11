import uuid

from sqlalchemy import Column, ForeignKey, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

import models.users
import app

class GlobalMessage(app.db.Model):
    __tablename__ = 'global_messages'

    db = app.db 

    id = db.Column(db.String(255), primary_key = True)
    message = db.Column (db.String(255))
    message_date = db.Column(db.DATETIME)
    user_id = db.Column(db.String(255), db.ForeignKey('users.id'))
    user = db.relationship("User", back_populates = "global_messages")

    def __init__(self, message, user_id, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.id = str(uuid.uuid4())
        self.message = message
        self.message_date = datetime.now()
        self.user_id = user_id

    def to_json(self, type: str = 'show'):
        if type == 'show':
            return {
                'id': self.id,
                'message': self.message,
                'message_date': self.message_date,
                'user_id': self.user_id
            }
        
        elif type == 'list':
            return {
                'id': self.id,
                'message': self.message,
            }
