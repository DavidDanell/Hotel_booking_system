from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, Enum as SAEnum, DECIMAL, DateTime, ForeignKey, Boolean, Date
from models.base import Base
from models.typings import Extra_beds
from datetime import datetime, date


class Booking(MappedAsDataclass, Base):
    __tablename__= 'bookings'

    id: Mapped[int]= mapped_column(Integer, primary_key= True, init= False)
    room_id: Mapped[int]= mapped_column(Integer, ForeignKey('rooms.id'), nullable= False)
    guest_id: Mapped[int]= mapped_column(Integer, ForeignKey('guests.id'), nullable= False)
    check_in_date: Mapped[date]= mapped_column(Date, nullable= False)
    check_out_date: Mapped[date]= mapped_column(Date, nullable= False)
    number_of_people: Mapped[int]= mapped_column(Integer, nullable= False)
    price: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)
    extra_beds: Mapped[Extra_beds]= mapped_column(SAEnum(Extra_beds, name= "extra_beds"), nullable= False)
    booked_at: Mapped[datetime]= mapped_column(DateTime, default= datetime.utcnow, nullable= False, init= False)
    is_cancelled: Mapped[bool]= mapped_column(Boolean, default=False, nullable= False, init= False)

    guest: Mapped["Guest"] = relationship(back_populates= 'bookings', init= False, uselist= False)
    room: Mapped["Room"] = relationship(back_populates= 'bookings', init= False, uselist= False)
    invoice: Mapped["Invoice"] = relationship(back_populates= 'booking', init= False, uselist= False)
