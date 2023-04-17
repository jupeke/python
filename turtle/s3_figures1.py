import turtle
def line():
    turtle.forward(200)
        

def square():
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)

def triangle():
    for x in range(3):
        turtle.forward(200)
        turtle.right(120)

def hexagon():
    for x in range(6):
        turtle.forward(100)
        turtle.right(60)

def dstar():
    for x in range(5):
        turtle.forward(200)
        turtle.right(144)

# Go to (x,y) without drawing a line:
def jumpto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

width = 800
height = 800
screen = turtle.getscreen()
screen.setup(width, height)

jumpto(-300,350)
line()
jumpto(100,350)
square()
jumpto(-300, 50)
triangle()
jumpto(150, 50)
hexagon()
jumpto(-100,-200)
dstar()

turtle. Screen(). exitonclick()