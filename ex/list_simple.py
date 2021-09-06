# Creates e new list:
list1 = ["Jani", "Arto", "Mari", "Maija"]
print() # An empty line.

print("Default print:")
print(list1)
print() # An empty line.

print("First element printed:")
print(list1[0])
print() # An empty line.

print("Last element printed:")
print(list1[-1])
print() # An empty line.

print("Elements preceded by a number:")
counter = 1
for elem in list1:
    print (counter,":", elem)   # Method 1: adds spaces around ":"!
    print (str(counter) + ": " + elem) # Method 2
    print ("{}: {}".format(counter, elem)) # Method 3
    counter = counter + 1
