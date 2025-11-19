from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, Enum, DECIMAL, Date, Boolean, ForeignKey
from database import Base, engine



class Room(Base):
    __tablename__= 'Rooms'

    id= mapped_column(Integer, primary_key= True)
    room_number= mapped_column(Integer, unique= True, nullable= False)
    number_of_beds= mapped_column(Enum('single_bed', 'double_bed'), nullable= False)
    possible_extra_beds= mapped_column(Enum('1', '2', '0'), nullable= False)
    price_per_night= mapped_column(DECIMAL(10, 2), nullable= False)


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
    extra_beds= mapped_column(Enum('1', '2', '0'), nullable= False)


class Invoice(Base):
    __tablename__= 'Invoices'
    id= mapped_column(String(35), primary_key= True)
    booking_id= mapped_column('booking_id', Integer, ForeignKey('Bookings.id'))
    total_amount= mapped_column(DECIMAL(10, 2), nullable= False)
    issue_date= mapped_column(Date, nullable= False)
    end_date= mapped_column(Date, nullable= False)
    is_paid= mapped_column(Boolean, nullable= False)


Base.metadata.create_all(engine)