from sqlalchemy import *
from sqlalchemy.orm import * 
from sqlalchemy.ext.declarative import declarative_base
from models import *

Base = declarative_base()

engine = create_engine('sqlite:///sitesdb', echo=True)

Base.metadata.create_all(engine)    




