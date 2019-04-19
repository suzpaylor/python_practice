soda = ["Coke", "Pepsi", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["chocolate", "skittles", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, CHIPS or CANDY? ").lower()
    
    try:
        if choice == 'soda':
            snack = soda.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We are all out of {}! Sorry".format(choice))
    else:    
        print("Here's your {}: {}".format(choice, snack))