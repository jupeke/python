from lib import *
#print("What's your name?")
#answer = input()
#print("Nice to see you, "+ answer)


print()
input1 = input("Give a number ")
input2 = input("Give another number ")

# Good?
result1 = input1 + input2

printnicemini("The sum of the inputs:")
printnicemini("{} + {} = {}".format(input1, input2, result1))

try:
    number1 = int(input1)   # Error if input not a whole number
    number2 = int(input2)   # Error if input not a whole number
    result2 = number1 + number2
    printnicemini("The sum of the numbers: {} + {} = {}".format(number1, number2, result2))
except ValueError:
    print("Error: one of the inputs is not an integer!")


























print()
'''
number1 = int(input1)
number2 = int(input2)
result2 = number1 + number2
printnicemini("The sum of the numbers: {} + {} = {}".format(number1, number2, result2))
'''




'''
# Better: if ValueError, goes to except block.
try:
    number1 = int(input1)   # Error if input not a whole number
    number2 = int(input2)   # Error if input not a whole number
    result2 = number1 + number2
    printnicemini("The sum of the numbers: {} + {} = {}".format(number1, number2, result2))
except ValueError:
    print("Error: one of the inputs is not an integer!")

'''