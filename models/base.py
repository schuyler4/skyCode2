from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

Base = declarative_base()

import models.user
#from Code import Project

engine = create_engine("sqlite:///data.db")
Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
db_session = Session()

#Base.query = db_session.query_property()
