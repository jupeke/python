def myfunc(a):
    return "Hihi"+a
def koe4():
    res = ""
    for i in range(4):
        res += "hi"
    return res

def koe5():
    res = ""
    counter = 0
    for i in range(4):
        if(counter == 1):
            res += "ti"
        else:
            res += "ta"
        counter += 1
    return res

def koe6():
    res = ""
    counter = 0
    for i in range(10):
        if(counter < 5):
            res += "HA"
        else:
            res += "HO"
        counter += 1
    return res

def add(a,b):
    return a+b

def showmess(numb, separ, mess):
    res = ""
    if(numb < 0):
        res = "Bad number!"
    else:
        for i in range(numb):
            res += mess+separ
    return res

def test1():
    txt = ""
    for i in range(3):
        txt += "piip"
    res = myfunc("juu")+txt
    stud = ["Peter", "Eva", "Maria"]
    res += "\n"
    res += stud[1]
    res += "\n"
    res += koe4()
    res += "\n"
    res += koe5()
    res += "\n"
    res += koe6()
    res += "\n"
    res += str(add(1,2))
    res += "\n"
    res += str(showmess(-1, " ", "Wow"))
    res += "\n"
    res += str(showmess(3, "  ", "Good work!"))
    res += "\n"
    res += str(showmess(5, "\n", "I love programming!"))
    return res

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
functions = [f1, f2, test1]
counter = 1
for f in functions:
    print()
    print("Function "+str(counter)+": "+f())
    counter += 1
