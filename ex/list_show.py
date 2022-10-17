# Create a list:
list1 = ["Jani", "Arto"]

# Add element:
list1.append("Emma")

# Print element (default format):
print(list1)

# Remove element at index i (if omitted removes the last element)
list1.pop(1)

print(list1)

# Custom print example:
output = ""
for item in list1:
    output += item+" "

print (output)


