finish = False
while finish == False:
    print() # Adds a line break. Looks nicer.
    print("Give a message, please:")
    # Retrieves the message given by user:
    message = input()
    print("You wrote: "+message);
    
    # To continue? Note the alternative syntax:
    m = input("Want to try again (yes/no)? ")
    if (m == "no"):
        finish = True
    elif (m == "yes" ):
        finish = False
    else:
        print("I don't understand you!")
        finish = False
