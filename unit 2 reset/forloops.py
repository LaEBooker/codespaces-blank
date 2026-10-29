# What is a loops --> code that repeats

# While loops = a block of code that repeats itself until the triggering 
# condition is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop BUT
# it only repeats itself upto a certain number of times.
# It is finite!

# Think of For loops as a counting loop

# FOR LOOP SYNTAX
# i stand for intertator = programmers decided make this the universal
# symbol for a placeholder for counting
#def counting():
    # this is what i want you to do..

for i in range(1,590):
    print(i)

for i in "school":
    print(i)

# LIST --> A collection type that acts as a container for
# multiple data types and pieces of data.

# List syntax
# A list is written like a variable BUT water the = we use
# square brackets [] and put all of the data inside
# of them

foodList = ['popcorn','chicken','bread','berries','pepper']

for i in foodList:
    print('i need to by' +str(i))

itemPrices = [10.00, 20.00, 13.25, 349.00]
tax = 0.07

for i in itemPrices:
    print('you will pay this in tax' + str(tax *i))

GradeSem = [90,100,79,87,75,84]

for i in GradeSem:
    if i < 85:
        print(i)

