from models import Base, Member
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
import datetime

# Create engine
db_uri = 'sqlite:///Ex2.db'
engine = create_engine(db_uri, echo=False)

#Create All Tables 
#Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine) 
session = Session()

user = Member(
    name='toddy',
    description='im testing this', 
    vip=True,
    join_date=datetime.datetime.now(), 
    number=45.0
)
user1 = Member(
    name='tody2',
    description='im testing this2', 
    vip=True,
    join_date=datetime.datetime.now(), 
    number=45.0
)
user2 = Member(
    name='tody3',
    description='im testing this3', 
    vip=True,
    join_date=datetime.datetime.now(), 
    number=45.0
)
user3 = Member(
    name='tody4',
    description='im testing this4', 
    vip=True,
    join_date=datetime.datetime.now(), 
    number=45.0
)
obj = session.query(Member).filter(Member.id==2).update({Member.name:'Johnson'})

session.commit() 
#print(user, user1, user2, user3)