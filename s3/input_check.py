print("How old are you (whole number)?")
# Test the value. If not a whole number, (ValueError), go to except block.
try:
    age = int(input())  # Error if input not good
    print("You are {} years old.".format(age))
except ValueError:
    print("Bad value!")
