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
    print (counter,":", elem)
    print (str(counter) + ": " + elem)
    print ("{}: {}".format(counter, elem))

    counter = counter + 1

print() # An empty line.
