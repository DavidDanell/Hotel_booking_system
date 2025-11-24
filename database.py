from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


my_url= "mysql+pymysql://root:cucumba@localhost:3306/hotel"
engine = create_engine(my_url) #
Session = sessionmaker(bind= engine)
session= Session()


class Base(DeclarativeBase):
    pass

#Base = declarative_base()

#SessionLocal= sessionmaker(bind = engine)