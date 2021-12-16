# Note: works well in python3 only!

# A function that prints the message a number of times:
def printmyname(namelist):
    print() # An empty line first. Looks better.
    for i in range(number):
        # Adds a growing number before the message:
        print(str(i+1)+": ",message)
    print() # An empty line.

finish = False
while finish == False:
    print() # Adds a line break. Looks nicer.
    print("Give a message, please:")
    # Retrieves the message given by user:
    message = input()
    print("Give a number, please")
    # Important: if ValueError, goes to except block.
    try:
        number = int(input())   # Error if input not good
        printmyname(message, number) # Function call
    except ValueError:
        print("Not an integer!")

    # To continue? Note the alternative syntax:
    m = input("Want to try again (yes/no)? ")
    if (m == "no"):
        finish = True
    elif (m == "yes" ):
        finish = False
    else:
        print("I don't understand you!")
        finish = False
