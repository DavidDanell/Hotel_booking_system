from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, Enum as SAEnum, DECIMAL, ForeignKey
from models.base import Base
from models.typings import Bed_type, Extra_beds
from database.db import Session




class Room(MappedAsDataclass, Base):
    __tablename__= 'Rooms'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_number: Mapped[int]= mapped_column(Integer, unique= True, nullable= False, init= True)
    number_of_beds: Mapped[Bed_type]= mapped_column(SAEnum(Bed_type), nullable= False, init= True)
    possible_extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds), nullable= False, init= True)
    price_per_night: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False, init= True)

    bookings: Mapped[list["Booking"]] = relationship(back_populates= 'room', init= False)

    def __repr__(self) -> str:
        return f'id: {self.id}, room number: {self.room_number}, bed type: {self.number_of_beds.name}, possible extra beds: {self.possible_extra_beds.name}, price/ night: {self.price_per_night} kr'
    
    
        



