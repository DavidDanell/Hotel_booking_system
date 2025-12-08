from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, Enum as SAEnum, DECIMAL, DateTime, ForeignKey, Boolean
from models.base import Base
from models.typings import Extra_beds
from datetime import datetime


class Booking(MappedAsDataclass, Base):
    __tablename__= 'Bookings'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_id: Mapped[int]= mapped_column(Integer, ForeignKey('Rooms.id'), nullable= False)
    guest_id: Mapped[int]= mapped_column(Integer, ForeignKey('Guests.id'), nullable= False)
    check_in_date: Mapped[datetime]= mapped_column(DateTime, nullable= False)
    check_out_date: Mapped[datetime]= mapped_column(DateTime, nullable= False)
    number_of_people: Mapped[int]= mapped_column(Integer, nullable= False)
    price: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)
    extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds), nullable= False)
    booked_at: Mapped[datetime]= mapped_column(DateTime, default= datetime.utcnow, nullable= False, init= False)
    is_cancelled: Mapped[bool]= mapped_column(Boolean, default=False, nullable= False, init= False)

    guest: Mapped["Guest"] = relationship(back_populates= 'bookings', init= False, uselist= False)
    room: Mapped["Room"] = relationship(back_populates= 'bookings', init= False, uselist= False)
    invoice: Mapped["Invoice"] = relationship(back_populates= 'bookings', init= False, uselist= False)
