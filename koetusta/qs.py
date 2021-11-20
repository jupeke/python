def f1():
    a = "hihi"
    return a

def f2():
    a = "hihi"
    return "hihi"+a

def f3():
    a = 3
    result = ""
    for i in range(a):
        result += "hihi"
    return result

def f4():
    res = ""
    counter = 0
    for i in range(4):
        if(counter == 1):
            res += "ti"
        else:
            res += "ta"
        counter += 1
    return res

def f5():
    res = ""
    counter = 0
    for i in range(4):
        if(counter < 2):
            res += "ta"
        else:
            res += "ti"
        counter += 1
    return res

def f6():
    students = ["Leila", "Adam", "Maria"]
    res = ""
    index = 0
    for name in students:
        numb_of_students = len(students)
        res += students[index]
        if(name == students[numb_of_students-1]):
            res += " is always late"
        else:
            res += " works well and "
        index = index+1
    return res

class Dog:
    def __init__(self, name, color, masskg):
        self.name = name
        self.color = color
        self.mass = masskg

    # Description of the dog:
    def desc (self):
        mass_in_str = str(self.mass)
        return "\n Name: "+self.name+", color: "+ \
            self.color+", mass: "+ mass_in_str+" kg"


def f7():
    dogs = [
        Dog("Tessu", "red", 20),
        Dog("Monsteri", "black", 53),
        Dog("Kasperi", "brown", 9),
        Dog("Aslak", "green", 29),
        Dog("Diva", "pink", 2),
    ]
    desc = ""
    #===================================================#
    # Write the code that makes this work!              #
    #                                                   #
    #                                                   #
    #===================================================#
    return desc

def f7_done():
    dogs = [
        Dog("Tessu", "red", 20),
        Dog("Monsteri", "black", 53),
        Dog("Kasperi", "brown", 9),
        Dog("Aslak", "green", 29),
        Dog("Diva", "pink", 2),
    ]
    desc = ""
    for hundi in dogs:
        desc += hundi.desc()
    return desc

def repeat_text(text, separator, number):
    res = ""
    counter = 0
    for i in range(number):
        if(counter > 0):
            res += separator
        res += text
        counter = counter+1
    return res

def test():
    print()
    text = input("text?")
    separ = input("separator?")
    numb = int(input("how many times?"))
    #print(repeat_text(text, separ, numb)) Students should have sthing like this
    return repeat_text(text, separ, numb)

functions2 = [f1, f2, f3, f4, f5, f6, f7_done, test]
#===============================================================================

def koe5():
    result = ""
    counter = 0
    for i in range(4):
        if(counter == 1):
            result += "ti"
        else:
            res += "ta"
        counter += 1
    return res

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

def func1():
    res = ""
    for i in range(3):
        res += "Hello"
    return res

def func2():
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
functions1 = [func1, func2, test1]


#===============================================================================
counter = 1
print()
for f in functions2:

    print("Function f"+str(counter)+": "+f())
    counter += 1
print()
