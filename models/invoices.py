from sqlalchemy.orm import mapped_column, relationship, Mapped, MappedAsDataclass
from sqlalchemy import Integer, String, Enum as SAEnum, DECIMAL, Date, Boolean, ForeignKey
from models.base import Base




class Invoice(MappedAsDataclass, Base):
    __tablename__= 'Invoices'
    id: Mapped[int]= mapped_column(String(35), primary_key= True, init= False)
    booking_id: Mapped[ForeignKey]= mapped_column(Integer, ForeignKey('Bookings.id'), init= False, nullable= False, unique= True)
    total_amount: Mapped[float]= mapped_column(DECIMAL(10, 2), nullable= False)
    issue_date: Mapped[Date]= mapped_column(Date, nullable= False)
    end_date: Mapped[Date]= mapped_column(Date, nullable= False)
    is_paid: Mapped[bool]= mapped_column(Boolean, nullable= False)

    booking: Mapped["Booking"] = relationship(back_populates= 'invoice', uselist= False, init= False)
