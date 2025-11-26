from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, Enum as SAEnum, DECIMAL, Date, ForeignKey
from models.base import Base
from models.typings import Extra_beds



class Booking(MappedAsDataclass, Base):
    __tablename__= 'Bookings'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_id: Mapped[ForeignKey]= mapped_column('room_id', Integer, ForeignKey('Rooms.id'), init= False)
    guest_id: Mapped[ForeignKey]= mapped_column('guest_id', Integer, ForeignKey('Guests.id'), init= False)
    check_in_date: Mapped[Date]= mapped_column(Date, nullable= False)
    check_out_date: Mapped[Date]= mapped_column(Date, nullable= False)
    number_of_people: Mapped[int]= mapped_column(Integer, nullable= False)
    price: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)
    extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds), nullable= False)



