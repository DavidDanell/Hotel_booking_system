from models.bookings import Booking
from datetime import datetime, date
from database.db import Session
from models.typings import Extra_beds, Bed_type
from models.guest import Guest
from models.invoices import Invoice
from models.rooms import Room


def create_booking(
    guest_id: int,
    room_id: int,
    check_in: date,
    check_out: date,
    number_of_people: int,
    extra_beds: Extra_beds
)-> Booking | None:
    
    if check_out <= check_in:
        print('Checkout date must be after checkin date!')
        return None
    
    
    with Session() as session:
        
        room= session.get(Room, room_id)
        if not room:
            print("Room with id:", {room_id}, "doesn't exist!")
            return None
        
        guest= session.get(Guest, guest_id)
        if not guest:
            print(f"Guest with id: {guest_id} doesn't exist!")
            return None
        
        overlapping = session.query(Booking).filter(
            Booking.room_id == room_id,
            Booking.check_out_date > check_in,
            Booking.check_in_date < check_out
        ).first()

        if overlapping:
            print('Room is already booked for these dates!')
            return None
        
        nr_of_nights= (check_out - check_in).days
        total_price= nr_of_nights * float(room.price_per_night)

        try:
            booking= Booking(
                guest_id= guest_id,
                room_id= room_id,
                check_in_date= check_in,
                check_out_date= check_out,
                number_of_people= number_of_people,
                price= total_price,
                extra_beds= extra_beds
            )

            
            session.add(booking)
            session.flush()

            
            invoice= Invoice(
                id= str(booking.id),
                booking_id= booking.id,
                total_amount= total_price,
                issue_date= check_in,
                end_date= check_out,
                is_paid=False
            )

            session.add(invoice)
            session.commit()
            session.refresh(booking)
            return booking
        except:
            print('Something went wrong with creating booking!')
            session.rollback()
            return None
        