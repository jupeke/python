import lib
def repeat_mess(number, message):
    output = ""
    counter = 0
    while counter < number:
        output += message + "\n"
        counter = counter + 1
    return output

lib.nice(repeat_mess(12, "Ok?"))