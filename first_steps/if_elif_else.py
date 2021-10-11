import random
my_age = round(random.random()*100)

if my_age==50:
    print("You are 50 years old")
elif my_age < 50:
    print("You are young ("+str(my_age)+" years)")
else:
    print("You are experienced (",my_age," years)")
