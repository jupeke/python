print()
input1 = input("Give a number ")
input2 = input("Give another number ")

# Good?
result1 = input1 + input2

print("The sum of the inputs: {} + {} = {}".format(input1, input2, result1))

# Better: try to convert the input strings into integers:
try:
    number1 = int(input1)   # Error if input not a whole number
    number2 = int(input2)   # Error if input not a whole number
    result2 = number1 + number2
    print("The sum of the numbers: {} + {} = {}".format(number1, number2, result2))
except ValueError:
    print("Error: one of the inputs is not an integer!")