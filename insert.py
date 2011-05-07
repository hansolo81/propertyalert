from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper, relation, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models import *
from sites import iproperty, fullhouse

engine = create_engine('sqlite:///sitesdb', echo=True)
metadata = MetaData(bind=engine)

stateslist = {'KL': ['Keramat', 'Wangsa Maju', 'Ampang'],
              'Selangor': ['Shah Alam', 'Petaling Jaya']
             }


Session = sessionmaker(bind=engine)
session = Session()

for state in stateslist:
    state_cities  = []

    for city in stateslist[state]:
        newcity = City(name=city, code=city)
        state_cities.append(newcity)
    
    newstate = State(name=state, code=state, cities = state_cities)

    session.add(newstate)

sites = []
site1 = Site(name='iproperty', url=iproperty.url, 
             formaction=iproperty.formaction, isform=iproperty.isform, 
             formname=iproperty.formname, xpath=iproperty.xpath, 
             params=iproperty.params)

site2 = Site(name='fullhouse', url=fullhouse.url, 
             formaction=fullhouse.formaction, isform=fullhouse.isform, 
             formname=fullhouse.formname, xpath=fullhouse.xpath, 
             params=fullhouse.params)

sites.append(site1)
sites.append(site2)

searches = []
searches.append(Search(site_id=1, params={'proptype_param':'r', 
                                          'state_param':'KL',
                                          'city_param':'Wangsa+Maju'}))

for s in sites:
    session.add(s)

for s in searches:
    session.add(s)

session.commit()
    
    




