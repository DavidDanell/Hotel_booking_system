


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