from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper, relation, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///sitesdb', echo=True)
metadata = MetaData(bind=engine)

stateslist = {'KL': ['Keramat', 'Wangsa Maju', 'Ampang'],
              'Selangor': ['Shah Alam', 'Petaling Jaya']
             }

#states = Table('state', metadata, autoload=True)
#cities = Table('city', metadata, autoload=True)

Session = sessionmaker(bind=engine)
session = Session()

class City(Base):
    __tablename__ = 'city'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(40))
    code = Column('code', String(5), nullable=True)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
    #state = relationship(State, backref=backref("cities", order_by=id))

    def __init__(self, name=None, code=None):
        self.name = name
        self.code = code

    def __repr__(self):
        return self.name

class State(Base):
    __tablename__ = 'state'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(40))
    code = Column('code', String(5), nullable=True)
    cities = relationship(City, backref="state")

    def __init__(self, name=None, code=None, cities=[]):
        self.name = name
        self.code = code
        self.cities = cities

    def __repr__(self):
        return self.name


#citymapper = mapper(City, cities)
#statemapper = mapper(State, states, properties={'cities': relation(citymapper),})

for state in stateslist:
    state_cities  = []

    for city in stateslist[state]:
        newcity = City(name=city, code=city)
        state_cities.append(newcity)
    
    newstate = State(name=state, code=state, cities = state_cities)

    session.add(newstate)
session.commit()
    
    




