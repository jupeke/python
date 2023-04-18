import turtle

# Class definition:
class Artist:
    t = turtle.Turtle()

    def __init__(self, pcolor, fcolor, psize, speed):
        self.t.pen(pencolor = pcolor, fillcolor = fcolor, 
                   pensize = psize, speed = speed)

    def setcolor(self, newcolor):
        self.t.pen(pencolor = newcolor)
    def setfillcolor(self, newcolor):
        self.t.pen(fillcolor = newcolor)
    def setpensize(self, newsize):
        self.t.pen(pensize = newsize)
    def setspeed(self, newspeed):
        self.t.pen(speed = newspeed)
    def getcolor(self):
        return self.t.pencolor  
    def getfillcolor(self):
        return self.t.fillcolor
    def getpensize(self):
        return self.t.pensize
    
    # Go to (x,y) without drawing a line:
    def jumpto(self, x,y):
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()

    def line(startx, starty):
    jumpto(startx,starty)
    t.forward(200)

    def square(self, fillme,startx, starty, len):
        jumpto(startx,starty)
        if fillme:
            self.t.begin_fill()
        for x in range(4):
            self.t.forward(len)
            self.right(90)
        if fillme:
            self.end_fill()


    def triangle(fillme,startx, starty):
        jumpto(startx,starty)
        if fillme:
            t.begin_fill()
        for x in range(3):
            t.forward(200)
            t.right(120)
        if fillme:
            t.end_fill()

    def hexagon(fillme,startx, starty):
        jumpto(startx,starty)
        if fillme:
            t.begin_fill()
        for x in range(6):
            t.forward(100)
            t.right(60)
        if fillme:
            t.end_fill()

    def dstar(fillme,startx, starty):
        jumpto(startx,starty)
        if fillme:
            t.begin_fill()
        for x in range(5):
            t.forward(200)
            t.right(144)
        if fillme:
            t.end_fill()

      
# Create instances of the Car class:
a = Artist("green", "lightblue", 5, 5)

t = turtle

t.pen(pencolor="brown", fillcolor="orange", 
      pensize=5, speed=3)

t.bgcolor("pink")

def line(startx, starty):
    jumpto(startx,starty)
    t.forward(200)

def square(fillme,startx, starty):
    jumpto(startx,starty)
    if fillme:
        t.begin_fill()
    for x in range(4):
        t.forward(200)
        t.right(90)
    if fillme:
        t.end_fill()


def triangle(fillme,startx, starty):
    jumpto(startx,starty)
    if fillme:
        t.begin_fill()
    for x in range(3):
        t.forward(200)
        t.right(120)
    if fillme:
        t.end_fill()

def hexagon(fillme,startx, starty):
    jumpto(startx,starty)
    if fillme:
        t.begin_fill()
    for x in range(6):
        t.forward(100)
        t.right(60)
    if fillme:
        t.end_fill()

def dstar(fillme,startx, starty):
    jumpto(startx,starty)
    if fillme:
        t.begin_fill()
    for x in range(5):
        t.forward(200)
        t.right(144)
    if fillme:
        t.end_fill()

# Go to (x,y) without drawing a line:
def jumpto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

width = 800
height = 800
screen = t.getscreen()
screen.setup(width, height)

fillme = True

line(-300,350)
square(fillme,100,350)
triangle(fillme,-300, 50)
hexagon(fillme,150, 50)
dstar(fillme,-100,-200)

t. Screen(). exitonclick()