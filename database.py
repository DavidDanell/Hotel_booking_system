from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


my_url= "mysql+pymysql://root:cucumba@localhost:3306/namn"
#engine = create_engine('sqlite:///Hotel.db', echo= True)

class Base(DeclarativeBase):
    pass

#Base = declarative_base()

#SessionLocal= sessionmaker(bind = engine)