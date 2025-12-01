from models.rooms import Room
from database.db import Session
from models.typings import Bed_type, Extra_beds


def add_room(room_number: int, bed_type: Bed_type, extra_beds: Extra_beds, price: int) -> Room | None:
    with Session() as func_session:
        
        existing_room = func_session.query(Room).filter_by(room_number = room_number).first()

        if existing_room:
            print("Det finns redan ett rum med detta nummer!")
            return existing_room
        
        new_room = Room(
            room_number=room_number,
            number_of_beds=bed_type,
            possible_extra_beds= extra_beds,
            price_per_night= price
        )

        func_session.add(new_room)
        func_session.commit()
        print(f'New room added: room number- {new_room.room_number}')