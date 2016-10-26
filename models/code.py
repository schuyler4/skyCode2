from sqlalchemy import *
from .base import Base
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))
    files = relationship('')

class Directory(Base):
    __tablename__ = "Directory"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))


class File(Base):
    __tablename__ = "File"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))
    
    
