from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper, relation, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models import *
from sites import iproperty, fullhouse, mudah

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

site3 = Site(name='mudah', url=mudah.url, 
             formaction=mudah.formaction, isform=mudah.isform, 
             formname=mudah.formname, xpath=mudah.xpath, 
             params=mudah.params)


sites.append(site1)
sites.append(site2)
sites.append(site3)

for s in sites:
    session.add(s)

session.add(User(firstname='han', lastname='solo', email='hansolo81@gmail.com'))
session.add(User(firstname='star', lastname='buck', email='shazzerin@yahoo.com'))

session.commit()
    
    




