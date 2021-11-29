def repeat_text(text,separator,number):
    a=(text+separator)*(number-1)
    return a+text

print(repeat_text("duck","&",5))
