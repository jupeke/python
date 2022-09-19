def format_nicely(content):
    print("--------------------------------")
    print()
    print(content)
    print()
    print("--------------------------------")

format_nicely("Hi you!")
format_nicely("This is something quite long!")

# A function that adds two numbers and returns the result:
def add_numbers(a,b):
    my_sum = a+b
    return my_sum

format_nicely(add_numbers(100,200))
format_nicely(add_numbers(10,20))
format_nicely(add_numbers(10345345345,3450))
