import random

#name = "Dan"
#print("What's your name?")
#name = input()
#print("Hi "+name)
'''
print("Give me a number")
# the command int is needed to convert a string into number.
number1 = int(input())
print("Give me another number")
number2 = int(input())

sum = number1 + number2

print("{} + {} = {}".format(number1, number2, sum))

result = ""
for i in range(number2):
    result += "{} ".format(number1)

print("Result: "+result)

print("Want to go on? (yes/no)")
ans = input()
if (ans == "yes"):
    print("Yes")
elif (ans == "no"):
    print("no")
else:
    print("I don't understand")
'''
print("My random number: {}".format(random.randint(0,100)))