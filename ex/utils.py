# A function that prints the message a number of times:
def repeat(message, number):
    print() # An empty line first. Looks better.
    for i in range(number):
        # Adds a growing number before the message:
        print(str(i+1)+": ",message)
    print() # An empty line.

# Returns a list of random integers between 0 and
# parametre "ceiling".
# There will be "len" elements on the list.
import random
def randomnumberlist(len, ceiling):
    randomlist = list()
    for i in range(len):
        # Appends an integer between 0 and ceiling
        # (both included)
        randomlist.append(random.randint(0, ceiling))
    return randomlist
