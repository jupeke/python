# A function that prints the message a number of 
# times with the separator not first not last:
def repeat_text(text, separator, number):
    print((text+separator) * (number-1) + text)

print(repeat_text("duck","&",5))

