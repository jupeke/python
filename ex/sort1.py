

# Returns a new list with the elements of list
# sorted in ascending order. This is one the
# first method that comes to mind with
# time requirement O(n^2). Preserves the
# original list.
def sort1(unsortedlist):
    ordererlist = list()
    # Makes a shallow copy of the orig list.
    workinglist = unsortedlist.copy()

    while (len(workinglist) != 0):
        smallest = workinglist[0]
        for int in workinglist:
            if(int < smallest):
                smallest = int
        ordererlist.append(smallest)
        workinglist.remove(smallest)
    return ordererlist

import utils
import timeit
mylist = utils.randomnumberlist(30, 20)

# Tests a sort function named "sort1"
print()
print("The original list:")
print(mylist)
print()
ordered1 = sort1(mylist)
print("The original list after using sort1:")
print(mylist)
print()
print("The list sorted by method sort1:")
print(ordered1)
