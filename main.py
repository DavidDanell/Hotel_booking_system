from database.db import Session
from models.bookings import Booking
from models.guest import Guest
from models.invoices import Invoice
from models.rooms import Room, add_room
from models.typings import Bed_type, Extra_beds
from database.db import Session



#rum=Room(4, Bed_type.SINGLE, Extra_beds.NONE, 300)
# add_room(1, Bed_type.SINGLE, Extra_beds.ONE, 300)
#session.add(rum)
#session.commit()
# rum1= session.query(Room).filter_by(room_number = 1).first()
#session.close()
# print(rum1)


add_room(4, Bed_type.SINGLE, Extra_beds.NONE, 300)
with Session() as session:
    while True:
        print('==============================\nVälkommen till hotellet!\n==============================')
        print('1. Boknings meny\n2. Adminmeny\n0. Avsluta')
        val = input('>>>')
        if val not in ('1', '2', '0'):
            print( 'Valet måste vara: "1", "2" eller "0"!')
            continue

        elif val == '0':
            print('Hejdå!')
            break

        elif val == '1':
            while True:
                print('==============================\nVälkommen till bokningsmenyn!\n==============================')
                print('1. Registrera ny kund\n2. Registrera en bokning\n3. Sök efter lediga rum\n0. Gå tillbaka')
                val = input('>>>')
                if val not in ('1', '2', '3', '0'):
                    print( 'Valet måste vara: "1", "2", "3" eller "0"!')
                    continue

                elif val =='0':
                    break

    pass