# This is done by chat.openai.com/chat application 
# following the given instructions. Not modified.
# 22.01.2023. The world is changing...
def repeat_text(text, separator, number):
    return separator.join([text] * number)

text = input("Enter a text: ")
separator = input("Enter a separator: ")
number = int(input("Enter a number: "))
print(repeat_text(text, separator, number))
