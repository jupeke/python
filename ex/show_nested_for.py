def square_of_strings(str, number):
    output = ""
    for k in range(number):
        for i in range(number):
            output += str
        output += "\n"  # Line break

    return output

print(square_of_strings("hi", 10))