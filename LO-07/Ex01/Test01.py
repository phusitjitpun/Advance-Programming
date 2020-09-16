import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Base, User

engine = create_engine('sqlite:///:memory:', echo=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bine=engine)
Session = Session()

user1 = User(name='user1', fullname='Ed Jones', nickname='ed')

session.add(user1)
session.commit()
