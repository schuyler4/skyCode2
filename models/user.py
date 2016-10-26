from sqlalchemy import *
from .base import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=true)
    username = Column(String(80), unique=True)
    password = Column(String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__ (self):
        return '<User %r>' % self.username

    
