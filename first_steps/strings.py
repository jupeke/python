# Function with two ways to concatenate strings, 
# adding an empty space between the strings.
def strings_together(a, b):
    result1 = ""
    result2 = ""
    # Method 1 with plus signs & quotes:
    result1 = "The final output: "+str(a)+" "+str(b);

    # Method 2 with format command:
    result2 = "The final output: {} {}".format(a,b);

    # Return the results of the two methods with a line break \n in between:
    return result1 +"\n"+result2

# Call the function to get real values:
output = strings_together(5, "messages")

print()     # This just adds an empty line -> nicer output 
print(output)
print()