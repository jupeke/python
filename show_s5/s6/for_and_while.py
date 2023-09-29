max = 10
result_for = ""
result_while = ""

# Repetition with "while":
current = 1
while current <= max:    
    result_while += "{} ".format(current)
    current += 1

# The same result using the structure "for"
for i in range(max):
    result_for += "{} ".format(i+1)

print("\n while loop: "+result_while)
print("\n for loop: "+result_for)
print()