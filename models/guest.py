from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, String, ForeignKey
from models.base import Base


class Guest(MappedAsDataclass, Base):
    __tablename__= 'Guests'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    first_name: Mapped[str]= mapped_column(String(100), nullable= False)
    second_name: Mapped[str]= mapped_column(String(100), nullable= False)
    email_address: Mapped[str]= mapped_column(String(250), unique= True, nullable= False)


