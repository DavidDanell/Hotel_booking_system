from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


my_url= "mysql+pymysql://root:cucumba@localhost:3306/hotel"
engine = create_engine(my_url) #
Session = sessionmaker(bind= engine)





