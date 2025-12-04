from database.db import Session
from models.rooms import Room
from models.guest import Guest
from faker import Faker
from models.typings import Extra_beds, Bed_type
import random

fake= Faker()

def seeding_rooms(nr_to_seed: int= 100)-> None:
    with Session() as session:
        number_of_rooms= session.query(Room).count()
        if number_of_rooms > 0:
                print('Rooms already seeded!')
                return 
        x=1
        for i in range(nr_to_seed):
            try:
                room= Room(
                    room_number= x,
                    price_per_night= fake.random_int(300, 1000),
                    number_of_beds= random.choice([Bed_type.SINGLE, Bed_type.DOUBLE]),
                    possible_extra_beds= random.choice([Extra_beds.NONE, Extra_beds.ONE, Extra_beds.TWO])
                )
                x+=1
                session.add(room)
                session.commit()

            except:
                print('Something went wrong with adding rooms!', i)
                session.rollback()
                return 
            

def seeding_guest(nr_of_guet: int= 50)-> None:
     with Session() as session:
        number_of_guests= session.query(Guest).count()
        if number_of_guests > 0:
            print('Guests already seeded!')
            return
        
        
        for i in range(nr_of_guet):
            try:
                guest= Guest(
                    first_name= fake.first_name(),
                    second_name= fake.last_name(),
                    email_address= fake.unique.ascii_email()
                )

                session.add(guest)
                session.commit()
            
            except:
                print('Something went wrong with adding guest!', i)
                session.rollback()
                return 
            


