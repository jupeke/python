def startriangle(n):
    stars = ""
    for i in range(n+1):
        # Empty spaces on the left. +1 just to make same padding.
        for k in range(n-i+1): 
            stars += " "
        for j in range(i):
            stars += "* "
        stars += "\n"
    return stars

finish = False
while finish == False:
    print() # Adds a line break. Looks nicer.
    print("Give the number of stars (width of the triangle), please:")
    # Important: if ValueError, goes to except block.
    try:
        number = int(input())   # Error if input not good
        print(startriangle(number)) # Function call
    except ValueError:
        print("Not an integer!")

    # To continue? Note the alternative syntax:
    m = input("Again (yes/no)? ")
    if (m == "no"):
        finish = True
    elif (m == "yes" ):
        finish = False
    else:
        print("I don't understand you!")
        finish = False
