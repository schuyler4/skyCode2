from sqlalchemy import *
from .base import Base
#from .user import User
from sqlalchemy.orm import relationship

class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey="User.id")
    user = relationship("User", back_populate="Projects")
    directorys = relationship('Directory', back_populate="Project")

    def __init__(self, name, user, user_id):
        self.name = name 
        self.user_id = user_id
        self.user = user

    def __repr__(self):
        return '<Project %r>' % self.name


class Directory(Base):
    __tablename__ = "Directory"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))
    project_id = Column(Integer, ForeignKey('Project.id'))
    project = relationship("Project", back_populate="Directory")
    files = relationship('File', back_populate="Project")

    def __init__(self, name, project, project_id):
        self.name = name
        self.project = project
        self.project_id = project_id

    def __repr__(self):
        return '<Directory %r>' % self.name

class File(Base):
    __tablename__ = "File"
    id = Column(Integer, primary_key=true)
    name = Column(String(80))
    code = Column(String())
    directory_id = Column(Integer, ForeignKey('Directory.id'))
    directory = relationship("Directory", back_populate="File")

    def __init__(self, name, directory_id, directory):
        self.name = name
        self.directory = directory
        self.directory_id = directory_id

    def __repr__(self):
        return '<File %r>' % self.name
    
    
