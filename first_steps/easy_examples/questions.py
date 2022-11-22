def f1():
    goon = True
    counter = 0
    result = ""
    while goon:
        if counter % 3 == 0:
            result += "A"
        else:
            result += "B"
        counter= counter+1
        if(counter == 10):
            goon = False
    return result
print(f1())

