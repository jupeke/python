from random import randint

randnumber = 0
max = 100
while randnumber != 5:
    randnumber = randint(1, max)    # random number between 1 and max.
    print(randnumber)

