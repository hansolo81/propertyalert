from sqlalchemy import *

engine = create_engine('sqlite:///sitesdb', echo=True)
metadata = MetaData(bind=engine)

states_table = Table('state', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('code', String(5)),
                    )

city_table = Table('city', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('state_id', None, ForeignKey('state.id')),
                  Column('name', String(40)),
                  Column('code', String(5)),
                  )

metadata.create_all()
  



