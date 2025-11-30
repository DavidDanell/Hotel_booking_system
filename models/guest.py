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



def add_guest(first_name, second_name, email_address) -> Guest | None:
    with Session() as funky_session:
        existing_guest = funky_session.query(Guest).filter_by(email_address = email_address).first()
        if existing_guest:
            print("Guest already exists!")
            return existing_guest

        new_guest = Guest(
            first_name= first_name,
            second_name= second_name,
            email_address= email_address
        )
        funky_session.add(new_guest)
        funky_session.commit()
        print(f'New guest added: {new_guest.first_name, new_guest.second_name}')



def is_valid_email(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
