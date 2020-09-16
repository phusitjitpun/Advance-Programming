import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Base, User

engine = create_engine('sqlite:///:memory:', echo=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bine=engine)
Session = Session()

for instance in session.query(User).filter(User.name.in_(('user1', 'user2'))):
    print(instance.name, instance.fullname)