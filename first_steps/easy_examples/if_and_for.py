import lib
def repeat_mess(number, message):
    output = ""
    for x in range(number):
        output += str(x+1)+": "+message
        if number > 5:
            output += "\n"
        else:
            output += " "
    return output

number = input("How many times?")
message = input("What message to repeat?")
lib.printnice(repeat_mess(int(number), message))