from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, String
from models.base import Base
from database.db import Session
from email_validator import validate_email, EmailNotValidError


class Guest(MappedAsDataclass, Base):
    __tablename__= 'Guests'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    first_name: Mapped[str]= mapped_column(String(100), nullable= False)
    second_name: Mapped[str]= mapped_column(String(100), nullable= False)
    email_address: Mapped[str]= mapped_column(String(250), unique= True, nullable= False)

    bookings: Mapped[list["Booking"]] = relationship(back_populates= 'guest', init= False)


