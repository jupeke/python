def f1():
    res = ""
    for i in range(3):
        res += "Hello"
    return res

def f2():
    a = "Hello "
    b = "my friend!"
    res = ""
    for i in range(2):
        if(i == 0):
            res += a
        else:
            res += b
    return res

# Testing functions:
functions = [f1, f2]
counter = 1
for f in functions:
    print()
    print("Function "+str(counter)+": "+f())
    counter += 1
