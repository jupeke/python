print("What's your name?")
answer = input()    # answer contains a string value
print("Hello "+answer)

print("Give me a number")
number1 = input()

print("Give me another number")
number2 = input()

# Sum of strings:
print("{} + {} = {}".format(number1, number2, number1+number2))

# Sum of numbers (integers):
n1 = int(number1)   # Convert string into number
n2 = int(number2)
sum = n1 + n2

print("{} + {} = {}".format(n1, n2, sum))