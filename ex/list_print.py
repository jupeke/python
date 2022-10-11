# Print the elements in your own way:
def showlist(comment,mylist):
    counter = 1
    output = comment+":\n"
    for elem in mylist:
        output += "{}: {} \n".format(counter, elem)
        counter = counter + 1   # Important!
    return output

# Create e new list:
list1 = ["Jani", "Arto", "Mari", "Maija"]
print() # An empty line.

print("Default print:")
print(list1)
print() 

print(showlist("Custom print",list1))

print("First element printed:")
print(list1[0])
print() 

print("Last element printed:")
print(list1[-1])
print() 

# Add an element to the end of the list:
list1.append("Student")
print(showlist("Student added:",list1))

# Remove the last element
list1.pop()
print(showlist("Last element removed",list1))

# Remove the third element
list1.pop(2)
print(showlist("The 3rd element removed",list1))
