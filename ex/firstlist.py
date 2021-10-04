# A real list to be printed:
list1 = ["Jani", "Arto", "Mari", "Maija"]

list1.append("Tiina")
list1.remove(1)

result = ""
for name in list1:
    result += name+" "

print(result)
