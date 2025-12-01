from database.db import Session
from models.guest import Guest
from email_validator import validate_email, EmailNotValidError


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