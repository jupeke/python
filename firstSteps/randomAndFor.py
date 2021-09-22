import random

#Declares and assign a value to the variable
randNumb = round(random.random() * 100)

for i in range(randNumb):
    print("Hello number "+ str(i+1))
