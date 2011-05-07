from sqlalchemy import *
from sqlalchemy.orm import * 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///sitesdb', echo=True)

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

class Site(Base):
    __tablename__ = 'site'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(40))
    url = Column('url', String(100))
    isform =Column('isform', Boolean())
    formname = Column('formname', String(40), nullable=True)
    formaction = Column('formaction', String(100), nullable=True)
    xpath = Column('xpath', String(200), nullable=True)
    state_param = Column('city_param', String(20), nullable=True)
    city_param = Column('state_param', String(20), nullable=True)
    range_param = Column('range_param', String(20), nullable=True)
    proptype_param = Column('proptype_param', String(20), nullable=True)

    def __init__(self, name=None, url=None, isform=None, formname=None, formaction=None, xpath=None, params={}):
        self.name = name
        self.url = url
        self.isform = isform
        self.formname = formname
        self.formaction = formaction
        self.xpath = xpath
        self.state_param = params.get('state_param')
        self.city_param = params.get('city_param')
        self.range_param = params.get('range_param')
        self.proptype_param = params.get('proptype_param')


    def __repr__(self):
        return self.name

class Search(Base):
    __tablename__ = 'search'

    id = Column('id', Integer, primary_key=True)
    
    state_param = Column('city_param', String(20), nullable=True)
    city_param = Column('state_param', String(20), nullable=True)
    range_param = Column('range_param', String(20), nullable=True)
    proptype_param = Column('proptype_param', String(20), nullable=True)
    site_id = Column(Integer, ForeignKey('site.id'), nullable=False)
    site = relationship(Site, backref=backref("searches", order_by=id))

    def __init__(self, site_id=None, params={}):
        self.site_id = site_id
        self.state_param = params.get('state_param')
        self.city_param = params.get('city_param')
        self.range_param = params.get('range_param')
        self.proptype_param = params.get('proptype_param')

    


Base.metadata.create_all(engine)    




