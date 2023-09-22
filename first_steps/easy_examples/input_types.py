from lib import *

print()
input1 = input("Give a number ")
input2 = input("Give another number ")

# Good?
result1 = input1 + input2

printnicemini("The sum of the inputs:")
printnicemini("{} + {} = {}".format(input1, input2, result1))

# Note: if ValueError, goes to except block.
try:
    number1 = int(input1)   # Error if input not a whole number
    number2 = int(input2)   # Error if input not a whole number
    result2 = number1 + number2
    printnicemini("The sum of the numbers:")
    printnicemini("{} + {} = {}".format(number1, number2, result2))

except ValueError:
    print("Error: one of the inputs is not an integer!")

print()
