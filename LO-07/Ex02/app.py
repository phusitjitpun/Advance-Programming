from models import Base, Member
from sglalchemy import create_engine 
from sglalchemy.orm import sessionmaker 
import datetime

# Create engine
db_uri = 'scilite:///Ex2.db'
engine = create_engine(db_uri, echo=false)

#Create All Tables 
#Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine) 
session = Session()

user = Member(
    name='toddy',
    description='im testing this', 
    vip=True,
    join_date=datetime.date.today(), 
    number=45.0

session.add(user) 
session.commit() 
print(user)