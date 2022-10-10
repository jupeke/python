# Note: works well in python3 only!
# Asks for a value with the question in parameter.
finish = False
while finish == False:
    print()
    message = input("Give a message, please: \n")

    # This way the input comes on its own row:
    print("Give a number, please")

    # Important: if ValueError, goes to except block.
    try:
        number = int(input())   # Error if input not good
        for i in range(number):
            print(str(i+1)+": ",message)
    except ValueError:
        print("Not an integer!")

    m = input("Want to try again (yes/no)? ")
    if (m != "yes"):
        finish = True
    print()
