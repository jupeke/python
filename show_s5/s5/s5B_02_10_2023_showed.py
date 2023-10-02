# A few examples of Python code
#print("What's your name?")

# Variable name to store the answer
#name = input()
#print("Hello "+name)

print("Give me a number")
number1 = input()   # Text!
print("Give me another number")
number2 = int(input())

sum = int(number1) + number2

# Use .format to put together strings, numbers and variables.
print("{} + {} = {}".format(number1, number2, sum))

# Options:
if (number2 > 20):
    print("The second number is greater than 20")
elif (number2 < 10):
    print("The second number is less than 10")
else:
    print("The second number is between 10 and 20")