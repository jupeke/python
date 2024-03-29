# Note: works well in python3 only!

# A function that prints the message a number of times:
def repeat(message, number):
    for i in range(number):
        # Adds a growing number before the message:
        print(str(i+1)+": ",message)

# A function that prints the message a number of times:
def repeat_string(text, separator, number):
    print((text+separator) * (number-1)+text)

finish = False
while finish == False:
    print() # Adds a line break. Looks nicer.
    print("Give a message, please:")
    # Retrieves the message given by user:
    message = input()
    print("Give a number, please:")
    # Important: if ValueError, goes to except block.
    try:
        number = int(input())   # Error if input not good
        repeat_string(message, " and ", number) # Function call
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
