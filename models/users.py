import uuid

from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, String
from werkzeug.security import generate_password_hash, check_password_hash
from models.base import Base

import models.messages
import app

class User(app.db.Model, UserMixin):
    __tablename__ = 'users'

    db = app.db

    id = db.Column(String(255), primary_key = True)
    username = db.Column(db.String(255), unique = True, nullable=False)
    email = db.Column(db.String(255), unique = True, nullable=False) 
    password = db.Column(db.String(255))
    connected = db.Column(db.Boolean)
    is_admin = db.Column(db.Boolean, default = False)
    global_messages = db.relationship("GlobalMessage", back_populates = "user")
    # messages_sent = relationship("Message", foreign_keys = "[Message.user_from_id]", back_populates = "user_to", overlaps="user_from")
    # messages_received = relationship("Message",  foreign_keys = "[Message.user_to_id]", back_populates = "user_from", overlaps="user_to")

    def __init__(self, username, email, password,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.id = str(uuid.uuid4())
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.connected = False

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self, type: str = 'obj'):
        if type == 'show':
            return {
                'id': self.id,
                'username': self.username,
                'email': self.email,
                'connected': self.connected,
                'is_admin': self.is_admin
            }
        
        elif type == 'list':
            return {
                'id': self.id,
                'username': self.username
            }

        elif type == 'obj':
            return {
                'id': self.id,
                'username': self.username,
                'email': self.email,
                'password': self.password,
                'connected': self.connected,
                'is_admin': self.is_admin
            }