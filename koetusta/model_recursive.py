def repeat_text(text,separator,number):
    if(number == 1):
        return text
    else:
        return repeat_text(text,separator,number-1)+ \
            separator+text

print(repeat_text("duck","&",5))
