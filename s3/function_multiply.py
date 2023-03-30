# Calculate product of two numbers:
def multiply(number1,number2):
    result = number1 * number2
    return result

print("Give a number")
n1 = int(input())
print("Give a second number")
n2 = int(input())

print("The product is {}".format(multiply(n1,n2)))

