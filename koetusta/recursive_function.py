''' # this works but is not very nice
def repeat_text(text,number):
    if(number == 1):
        return str(6-number)+": "+text
    else:
        return str(6-number)+": "+text+", "+repeat_text(text,number-1) 
'''
# Works also and is a bit nicer.
'''def repeat_text(text,number,counter):
    output = str(counter)+": "+text+"\n"
    if(number > 1):
        return output + repeat_text(text,number-1,counter+1) 
    return output
'''
def repeat_text(text,number,counter):
    text = str(counter)+": "+text+" "
    if(number > 1):
        return repeat_text(text,number-1,counter+1) 
    return text
print(repeat_text("duck",5,1))
