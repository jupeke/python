# Function to format the content in a nice way.
def nice(content):
    print("------------------------------------------------")
    print()
    print(content)
    print()
    print("------------------------------------------------")

# Call the function:
my_content = "This is some content"
nice(my_content)
nice("This is really amazing!")

# Function to sum up two numbers:
def sum_two_numbers(a,b):
    return a+b

nice(sum_two_numbers(11,22))
nice(sum_two_numbers(221,245))