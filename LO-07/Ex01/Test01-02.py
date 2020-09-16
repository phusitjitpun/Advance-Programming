import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Base, User

engine = create_engine('sqlite:///:memory:', echo=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bine=engine)
Session = Session()

user3 = User(name='user3', fullname='STEd Jones', nickname='STed')
user4 = User(name='user4', fullname='WTEd Jones', nickname='WTed')

session.add_all(user, user4)
session.commit()