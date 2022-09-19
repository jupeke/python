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
def randomnumberlist(len, ceiling):
    import random
    randomlist = list()
    for i in range(len):
        # Appends an integer between 0 and ceiling
        # (both included)
        randomlist.append(random.randint(0, ceiling))
    return randomlist

# Returns the name of the function as a string.
# This is not trivial!
def functionname(function):
    #import inspect
    #import types
    #from typing import cast
    #import sys
    #return inspect.currentframe().f_back.f_code.co_name
    #return sys._getframe(1).f_back.f_code.co_name
    return "not working"
#print(functionname(repeat("ih",3)))

# Returns a list of integers found in the string or an empty list if no found.
# NOT FINISHED
def get_ints_of_string(str):
    ints = list()
    return ints
