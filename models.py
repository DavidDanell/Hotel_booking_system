from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, String, Enum as SAEnum, DECIMAL, Date, Boolean, ForeignKey
from database import Base
from database import session
from enum import Enum

class Bed_type(Enum):
    SINGLE = 'single_bed'
    DOUBLE = 'double_bed'


class Extra_beds(Enum):
    NONE = '0'
    ONE = '1'
    TWO = '2'


class Room(MappedAsDataclass, Base):
    __tablename__= 'Rooms'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_number: Mapped[int]= mapped_column(Integer, unique= True, nullable= False)
    number_of_beds: Mapped[Bed_type]= mapped_column(SAEnum(Bed_type), nullable= False)
    possible_extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds), nullable= False)
    price_per_night: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)

    def __repr__(self) -> str:
        return f'id: {self.id}, room number: {self.room_number}, bed type: {self.number_of_beds.name}, possible extra beds: {self.possible_extra_beds.name}, price/ night: {self.price_per_night} kr'

class Guest(Base):
    __tablename__= 'Guests'

    id= mapped_column(Integer, primary_key= True)
    first_name= mapped_column(String(100), nullable= False)
    second_name= mapped_column(String(100), nullable= False)
    email_address= mapped_column(String(250), unique= True, nullable= False)


class Booking(Base):
    __tablename__= 'Bookings'

    id= mapped_column(Integer, primary_key= True)
    room_id= mapped_column('room_id', Integer, ForeignKey('Rooms.id'))
    guest_id= mapped_column('guest_id', Integer, ForeignKey('Guests.id'))
    check_in_date= mapped_column(Date, nullable= False)
    check_out_date= mapped_column(Date, nullable= False)
    number_of_people= mapped_column(Integer, nullable= False)
    price= mapped_column(DECIMAL(10, 2), nullable= False)
    extra_beds= mapped_column(SAEnum(Extra_beds), nullable= False)


class Invoice(Base):
    __tablename__= 'Invoices'
    id= mapped_column(String(35), primary_key= True)
    booking_id= mapped_column('booking_id', Integer, ForeignKey('Bookings.id'))
    total_amount= mapped_column(DECIMAL(10, 2), nullable= False)
    issue_date= mapped_column(Date, nullable= False)
    end_date= mapped_column(Date, nullable= False)
    is_paid= mapped_column(Boolean, nullable= False)



# room1 = Room(
#     room_number= 1,
#     number_of_beds = Bed_type.SINGLE,
#     possible_extra_beds = Extra_beds.ONE,
#     price_per_night = 300
#     )

# room2 = Room(
#     room_number= 2,
#     number_of_beds= Bed_type.DOUBLE,
#     possible_extra_beds= Extra_beds.TWO,
#     price_per_night= 500
# )

#session.add_all([room1, room2])
alla_rum = session.query(Room).all()

def add_room(room_number: int, bed_type: Bed_type, extra_beds: Extra_beds, price: int):
    existing_room = session.query(Room).filter_by(room_number = room_number).first()

    if existing_room:
        print("Det finns redan ett rum med detta nummer!")
        return existing_room
    
    new_room = Room(
        room_number=room_number,
        number_of_beds=bed_type,
        possible_extra_beds= extra_beds,
        price_per_night= price
    )

    session.add(new_room)
    session.commit()
    return F'New room added: room number- {new_room.room_number}'

add_room(1, Bed_type.SINGLE, Extra_beds.ONE, 300)

rum1= session.query(Room).filter_by(room_number = 1).first()

print(rum1)
#Base.metadata.create_all(engine)