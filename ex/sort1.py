import utils

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

mylist = utils.randomnumberlist(30, 20)

print("The original list:")
print(mylist)
ordered1 = sort1(mylist)
print("The original list after using sort1:")
print(mylist)
print("The list sorted by method sort1:")
print(ordered1)
