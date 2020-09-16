import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Base, User

engine = create_engine('sqlite:///user.db', echo=False)

#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine) #สร้างtable ตรงนี้

Session = sessionmaker(bind=engine)
session = Session() #มีsesion พร้อมใช้งาน

user2 = User(name='user2', fullname='TEd Jones', nickname='Ted')

session.add(user2)
session.commit() #save database
