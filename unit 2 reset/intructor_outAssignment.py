
def Dicegame():
    print('dice game')
    print('type R to roll the die or Q to quit')
    userSelection = input()

    while userSelection !='q':
        if userSelection == 'r':
            diceValue = random,randit(1,7)
            if diceValue == 7:
                print(' u rolled a..' + str(diceValue))
                print('u win ig')
                print('type R to roll the die or Q to quit')
                userSelection = input()
            else:
                print('u lose ig') 