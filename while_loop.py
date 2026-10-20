# loop- a loop is a construct (special function) that repeats itslef.
# In programing, a loop allows to repeat code instructions.

# There are two type of loops: For loop and While loop

# While loop- a type of loop where so long as a condition is equal
# to true it will keep running forever.

# the keyboard is while --> do while

# syntax
num = 4 
while 2+2 == num: #conditonal --> operations - must be true
    print('boingaloing...')
    num = int(input('please type a number:'))

# while loops will ALWAYS run unless you change the conditional!
# we can do this by writing instructions to manually change it.

def guessing_Game():
    correctAnswer = 9
    attemps = 0     
    print("game has started!")
    userGuess = int(input('please guess a number between 1 and 10'))

    while userGuess != correctAnswer:
        print('guess again cause u wrong')
        attemps +=1
        print('guess attemps: ' +str(attemps))
        userGuess = int(input('please guess a number between 1 and 10'))
    
    print('You guessed correct lil boy')

guessing_Game()

