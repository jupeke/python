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
def get_ints_of_string(mystr):
    ints = list()
    strlen = len(mystr)
    i = 0
    # i gives the start index of a slice, j the end index. Range starts from 0.
    while i < strlen:
        # initiates at every change of start index.
        candidate = -1
        for j in range(strlen):
            slice = mystr[i:j+1]  # Characters from i to j taken (j+1 is left out)
            if(slice.isdigit() and int(slice)>candidate):
                candidate = int(slice)
        # If int found starting at i:
        if(candidate != -1):
            ints.append(candidate)
            # If number consists of several digits, start index jumps to the
            # first non-decimal:
            i += len(str(candidate))
        else:
            # If no int found with that start index, tries the next one:
            i = i+1
    return ints

def test_get_ints_of_string():
    strs = ["", "1","12345", "a1a", "a1a2j","a1a123h","113f222",
            "3,4-4 g 9709","12a31h42a555", "8 x 9 = ?"]
    for str in strs:
        print("Testing string","\""+str+"\",","result:",get_ints_of_string(str))

test_get_ints_of_string()
