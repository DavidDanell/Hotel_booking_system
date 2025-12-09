from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, String, Enum as SAEnum, DECIMAL, Boolean, ForeignKey, DateTime
from models.base import Base
from datetime import datetime, timedelta

def calculate_end_date():
    return datetime.utcnow() + timedelta(days= 10)

class Invoice(MappedAsDataclass, Base):
    __tablename__= 'invoices'
    id: Mapped[str]= mapped_column(String(35), primary_key= True)
    booking_id: Mapped[int]= mapped_column(Integer, ForeignKey('bookings.id'), nullable= False, unique= True)
    total_amount: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)
    is_paid: Mapped[bool]= mapped_column(Boolean, nullable= False)
    issue_date: Mapped[datetime]= mapped_column(DateTime, default= datetime.utcnow, nullable= False, init=False)
    end_date: Mapped[datetime]= mapped_column(DateTime, default= calculate_end_date ,nullable= False, init=False)
    is_cancelled: Mapped[bool]= mapped_column(Boolean, nullable= False, default= False, init= False)

    booking: Mapped["Booking"] = relationship(back_populates= 'invoice', uselist= False, init= False)
