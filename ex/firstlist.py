# A real list to be printed:
list1 = ["Jani", "Arto", "Mari", "Maija"]

list1.append("Tiina")
list1.remove("Tiina")

result = ""
for name in list1:
    result += name+" "

print(result)
