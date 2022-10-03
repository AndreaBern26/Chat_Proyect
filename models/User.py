import uuid
from xmlrpc.client import Boolean

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean
from models.base import Base


class User(Base, UserMixin):
    
    __tablename__ = 'users'

    id = Column(String(255), primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255))
    connected = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    global_messages = relationship("GlobalMessages", back_populates="user")
    messages = relationship("Messages")


    def __init__(self, username, email, password, is_admin=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid4() #Genera una id aleatoria y única.
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
