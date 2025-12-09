from database.db import Session
from models.bookings import Booking
from services.booking_service import create_booking
from models.guest import Guest
from services.guest_service import add_guest, is_valid_email
from models.invoices import Invoice
from services.invoice_service import cancel_unpaid_bookings, unpaid_invoices, pay_invoice
from models.rooms import Room
from services.room_service import add_room, room_capacity, filter_rooms
from models.typings import Bed_type, Extra_beds
from datetime import date, datetime
from services.seeding import seeding_rooms, seeding_guest
from models.base import Base
from sqlalchemy import text

with Session() as session:
    session.query(Invoice).delete()
    session.query(Booking).delete()
    session.query(Room).delete()
    session.query(Guest).delete()
    

    session.commit()

    session.execute(text('ALTER TABLE invoices AUTO_INCREMENT = 1;'))
    session.execute(text('ALTER TABLE bookings AUTO_INCREMENT = 1;'))
    session.execute(text('ALTER TABLE rooms AUTO_INCREMENT = 1;'))
    session.execute(text('ALTER TABLE guests AUTO_INCREMENT = 1;'))
    
    session.commit()



with Session() as session:
    

    cancel_unpaid_bookings()
    seeding_rooms(100)
    seeding_guest(50)

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
                print('1. Registrera ny gäst\n2. Registrera en bokning\n3. Sök efter lediga rum\n0. Gå tillbaka')
                val = input('>>>')
                if val not in ('1', '2', '3', '0'):
                    print( 'Valet måste vara: "1", "2", "3" eller "0"!')
                    continue

                elif val =='0':
                    break

                if val == '1':
                    
                    firstname=input('Vad är gästens förnamn?: ')
                    if not firstname.isalpha():
                        print('Namn måste bestå av bokstäver!')
                        continue                          
                    
                    secondname=input('Vad är gästens efternamn?: ')
                    if not secondname.isalpha():
                        print('Namn måste bestå av bokstäver!')
                        continue

                    email=input('Vad är gästens email?: ')
                    koll=is_valid_email(email)
                    if not koll:
                        print('Emailen har ogiltigt format\nGiltigt format: "namn@outlook.com"')
                        continue
                    
                    add_guest(firstname, secondname, email)


                if val == '2':    
                    val= input('Skriv "ja" för att visa befintliga gäster, annars tryck enter för att gå vidare: ').lower()
                    if val == 'ja':
                        guests= session.query(Guest).all()
                        for people in guests:
                            print(people.id, people.first_name, people.second_name)

                    checkin= input('skriv check in datum, format:(YEAR,MM,DD): ')
                    checkout= input('skriv check ut datum, format:(YEAR,MM,DD): ')
                    try:
                        y1,m1,d1 = checkin.split(',')
                        y2,m2,d2 = checkout.split(',')

                        checkin= date(int(y1),int(m1),int(d1))
                        checkout= date(int(y2),int(m2),int(d2))
                    except ValueError:
                        print('Fel format på datum, försök igen!')
                        continue
                    
                    try:    
                        nrpeople= int(input('skriv antalet personer som vill bo i rummet: '))
                    except ValueError:
                        print('Antal personer måste vara en siffra!')
                        continue
                    occupied_during= session.query(Booking.room_id).filter(
                        Booking.check_in_date < checkout,
                        Booking.check_out_date > checkin,
                        Booking.is_cancelled == False
                        )
                    
                    avalible= session.query(Room).filter(
                        ~Room.id.in_(occupied_during)).all()
                    
                    acceptable_rooms= filter_rooms(avalible, nrpeople)

                    if not acceptable_rooms:
                        print('Det finns inga tillgängliga rum som passar dina önskemål.')    
                        continue
                    else:
                        print('Lediga rum för dina datum: ')
                        for r in acceptable_rooms:
                            if r:
                                print(f'Rum id: {r.id}, säng: {r.number_of_beds.name}, möjliga extra sängar: {r.possible_extra_beds.name}, pris per natt: ({r.price_per_night}-kr)')    

                    try:
                        guestid= int(input('Skriv gästens id: '))
                        roomid= int(input('Skriv vilket rum id du vill boka: '))
                        room_exist= False

                        for r in acceptable_rooms:
                            if r.id == roomid:
                                room_exist= True
                                break
                        
                        if not room_exist:    
                            print('Du valde ett rum som inte är tillgängligt, försök igen')
                            continue

                    except ValueError:
                        print('Gäst id och rum måste vara siffror!')
                        continue
                    
                   
                    
                    room= session.query(Room).filter(Room.id == roomid).first()
                    if nrpeople == 1:
                        extrabed= Extra_beds.NONE

                    if nrpeople == 2 and room.number_of_beds == Bed_type.SINGLE:
                        extrabed= Extra_beds.ONE
                    elif nrpeople == 2 and room.number_of_beds == Bed_type.DOUBLE:
                        extrabed= Extra_beds.NONE
                    
                    if nrpeople == 3 and room.number_of_beds == Bed_type.SINGLE:
                        extrabed= Extra_beds.TWO
                    elif nrpeople == 3 and room.number_of_beds == Bed_type.DOUBLE:
                        extrabed= Extra_beds.ONE

                    if nrpeople == 4:
                        extrabed= Extra_beds.TWO
                                        

                    try:
                        create_booking(guestid, roomid, checkin, checkout, nrpeople, extrabed)
                        print(f'Rum med id: {roomid} har bokats!')
                    except:
                        print('Fel vid bokning')
    
                if val == '3':
                    
                    date1= input('Från vilket datum vill du söka lediga rum? Format:"YYYY,MM,DD": ')
                    date2= input('Till vilket datum vill du söka lediga rum? Format:"YYYY,MM,DD": ')
                    persons= input('Antal personer: ')
                    

                    try:
                        persons= int(persons)
                    except ValueError:
                        print('personer måste vara en siffra!')
                        continue
                    try:
                        y1,m1,d1 = date1.split(',')
                        y2,m2,d2 = date2.split(',')

                        first= date(int(y1),int(m1),int(d1))
                        last= date(int(y2),int(m2),int(d2))
                    except ValueError:
                        print('Fel format på datum, försök igen!')
                        continue
                    
                    
                    occupied_rooms2= session.query(Booking.room_id).filter(Booking.check_in_date < last,
                                                                                Booking.check_out_date > first)
                    
                    avalible1= session.query(Room).filter(~Room.id.in_(occupied_rooms2)).all()

                    rooms= filter_rooms(avalible1, persons)
                    try:
                        for room1 in rooms:
                            print(f'Rum id: {room1.id}, säng: {room1.number_of_beds.name}, möjliga extra sängar: {room1.possible_extra_beds.name}')
                            if not room1:
                                print('Finns inga lediga rum för datumen!')
                    except TypeError:
                        ...

        elif val == "2":
            while True:
                print('==============================\nVälkommen till bokningsmenyn!\n==============================')
                print('1. Avboka bokning\n2. Registrera en betalning\n3. Visa Avbokade bokningar\n0. Gå tillbaka')
                val = input('>>>')
                if val not in ('1', '2', '3', '4', '0'):
                    print( 'Valet måste vara: "1", "2", "3", "4" eller "0"!')
                    continue

                elif val== "0":
                    break

                elif val == '1':
                    while True:
                        val1=input("Skriv boknings id för bokningen du vill avboka! ('0' för gå tillbaka)\n>>> ")
                        if val1== '0':
                            break
                        try:
                            val1=int(val1)
                        except ValueError:
                            print("Ogiltigt val. Måste vara ett giltigt id för en bokning!")
                            continue

                        booking=session.query(Booking).filter(Booking.id== val1).first()
                        if not booking:
                            print("Hittade inte en bokning med det id")
                            continue
                            
                            
                        booking.is_cancelled=True
                        booking.invoice.is_cancelled=True
                        session.commit()
                        print('Bokningen har avbokats!')
                        break



                        
    pass                