def Movie_Tickets():
    print('Welcome to the theater. Please enter your age')
    Age= int(input())
    if Age<7:
        print('This costs $8.00')
    elif Age> 8 and Age < 20:
        print('This cost $12.00')
    elif Age> 21 and Age < 60:
        print('This is $20.00')
    elif Age> 61:
        print("This ticket is free for you")
    else:
        print('sorry no ticket for youuuuu!!!')

def Signed_Permission_Slip():
    print('What yo grades lookin like young blood? you got ur slip signed? (Yes,No)')
    GPA= int(input(''))
    Signed_Permission_Slip()= int(input())
    if Signed_Permission_Slip == True:
        print('okok i see you got ur slip signed')
    elif GPA<90:
        print('no trip muddy bloody')
    else:
        print('go on yo trip.')

Signed_Permission_Slip()
