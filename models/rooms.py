from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, Enum as SAEnum, DECIMAL, ForeignKey
from models.base import Base
from models.typings import Bed_type, Extra_beds
from database.db import Session




class Room(MappedAsDataclass, Base):
    __tablename__= 'Rooms'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_number: Mapped[int]= mapped_column(Integer, unique= True, nullable= False)
    number_of_beds: Mapped[Bed_type]= mapped_column(SAEnum(Bed_type), nullable= False, init= True)
    possible_extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds), nullable= False, init= True)
    price_per_night: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)

    bookings: Mapped[list["Booking"]] = relationship(back_populates= 'room', init= False)

    def __repr__(self) -> str:
        return f'id: {self.id}, room number: {self.room_number}, bed type: {self.number_of_beds.name}, possible extra beds: {self.possible_extra_beds.name}, price/ night: {self.price_per_night} kr'
    
    # def __init__(
    #     self,
    #     room_number: int,
    #     number_of_beds: Bed_type,
    #     possible_extra_beds: Extra_beds,
    #     price_per_night: float
    #     ):
    #     """
    #     number_of_beds: Bed_type (Bed_type.SINGLE, Bed_type.DOUBLE)
    #     possible_extra_beds: Extra_beds (Extra_beds.NONE, Extra_beds.ONE, Extra_beds.TWO)
    #     """


    



def add_room(room_number: int, bed_type: Bed_type, extra_beds: Extra_beds, price: int):
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
        return f'New room added: room number- {new_room.room_number}'
    
        



