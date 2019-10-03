

# Returns a new list with the elements of list
# sorted in ascending order. This is one the
# first method that comes to mind with
# time requirement O(n^2). Note: destroys the
# original list.
def sort1(unsortedlist):
    ordererlist = list()
    while (len(unsortedlist) != 0):
        smallest = unsortedlist[0]
        for int in unsortedlist:
            if(int < smallest):
                smallest = int
        ordererlist.append(smallest)
        unsortedlist.remove(smallest)
    return ordererlist

import utils
mylist = utils.randomnumberlist(30, 20)

utils.test_sort1(mylist)
