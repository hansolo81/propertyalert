from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, mapper, relation, relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from models import *
from sites import iproperty, fullhouse

engine = create_engine('sqlite:///sitesdb', echo=True)
metadata = MetaData(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

searches = []
searches.append(Search(user_id=1, site_id=1, params={'proptype_param':'AR', 
                                          'searchtype_param':'R',
                                          'state_param':'KL',
                                          'city_param':'Wangsa+Maju',
                                          'range_param':'1'}))

searches.append(Search(user_id=1, site_id=1, params={'proptype_param':'AR', 
                                          'searchtype_param':'R',
                                          'state_param':'KL',
                                          'city_param':'Keramat',
                                          'range_param':'1'}))

searches.append(Search(user_id=1, site_id=2, params={'proptype_param':'r',
                                          'searchtype_param':'r',
                                          'state_param':'KL',
                                          'city_param':'461',
                                          }))

searches.append(Search(user_id=1, site_id=2, params={'proptype_param':'r',
                                          'searchtype_param':'r',
                                          'state_param':'KL',
                                          'city_param':'664',
                                          }))

searches.append(Search(user_id=1, site_id=3, params={'proptype_param':'2020',
                                          'searchtype_param':'u',
                                          'state_param':'1',
                                          'city_param':'Setiawangsa',
                                          }))


for s in searches:
    session.add(s)

session.commit()
    
    




