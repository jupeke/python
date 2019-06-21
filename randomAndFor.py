import random

#Declares and sets a variable
randNumb = round(random.random() * 100)

for i in range(randNumb):
    print("Hello number "+ str(i+1))
