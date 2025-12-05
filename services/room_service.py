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



def room_capacity(room: Room) -> int:
    
    base = 1 if room.number_of_beds == Bed_type.SINGLE else 2

    if room.possible_extra_beds == Extra_beds.NONE:
        extra = 0

    elif room.possible_extra_beds == Extra_beds.ONE:
        extra = 1

    elif room.possible_extra_beds ==  Extra_beds.TWO:
        extra = 2

    return base + extra


def filter_rooms(rooms, people: int) -> list[Room] | None:
    acceptable_rooms= []
    
    if people == 1:
        for room in rooms:
            acceptable_rooms.append(room)

        return acceptable_rooms
    
    elif people == 2:
        for room in rooms:
            if room_capacity(room) >= 2:
                acceptable_rooms.append(room)
        return acceptable_rooms

    elif people == 3:
        for room in rooms:
            if room_capacity(room) >= 3:
                acceptable_rooms.append(room)
        return acceptable_rooms
    
    elif people == 4:
        for room in rooms:
            if room_capacity(room) == 4:
                acceptable_rooms.append(room)
        return acceptable_rooms
    
    elif people >= 5:
        print('Det finns inga rum som kan hantera fler än 4 gäster, vänligen dela upp bokningen!')
        return

    else:
        print('Antalet personer måste vara en siffra!')
        return 