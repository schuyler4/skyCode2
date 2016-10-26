from sqlalchemy import *
from .base import Base
from .code import Project
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=true)
    username = Column(String(80), unique=True)
    password = Column(String(80))
    projects = relationship("Project", back_populates="User")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__ (self):
        return '<User %r>' % self.username

    
