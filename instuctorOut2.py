def vending_machine():
    while True:
        choice = input("Enter an item code (or q to quit): ").upper()

        if choice == "q".upper():
            print("preesh u")
            break
        elif choice == "B3":
            print("You got Nacho boy")
        elif choice == "G4":
            print("You got BBQ chips boy")
        elif choice == "G7":
            print("You got Plain Chips dirty")
        elif choice == "D3":
            print("You got Water bland boy")
        elif choice == "G5":
            print("You got Cola Soda hopefully dr.pepper")
        else:
            print("Invalid code. Please try again.")

vending_machine()
