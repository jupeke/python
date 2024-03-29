import turtle
import math

# Class definition:
class Artist:
    t = turtle.Turtle()
    turtle = turtle

    def __init__(self, pcolor, fcolor, psize, speed):
        self.t.pen(pencolor = pcolor, fillcolor = fcolor, 
                   pensize = psize, speed = speed)
        self.screenwidth = 800
        self.screenheight = 800
        self.screen = self.t.getscreen()
        self.screen.setup(self.screenwidth, self.screenheight)
    
    # Disables autoexit - the screen stays visible.
    def donotautoexit(self):
        self.turtle.mainloop()

    # Returns the x coordinate of the current position of the turtle
    def getx(self):
        return self.t.pos()[0]
    
    # Returns the y coordinate of the current position of the turtle
    def gety(self):
        return self.t.pos()[1]

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
    
    # Direction: "up", "down", "right", "left"
    def setdir(self, dir):
        if (dir == "up"):
            self.t.setheading(90)
        elif (dir == "right"):
            self.t.setheading(0)
        elif (dir == "down"):
            self.t.setheading(270)
        elif (dir == "left"):
            self.t.setheading(180)

    # Go to (x,y) without drawing a line:
    def jumpto(self, x,y):
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()

    def line(self, startx, starty, len):
        self.jumpto(startx,starty)
        self.t.forward(len)

    def square(self, fillme,cx, cy, sidelen):
        self.jumpto(int(cx-sidelen/2),int(cy+sidelen/2))
        if fillme:
            self.t.begin_fill()
        for x in range(4):
            self.t.forward(sidelen)
            self.t.right(90)
        if fillme:
            self.t.end_fill()

    def triangle(self, fillme,centerx, centery, sidelen):
        height = math.sqrt(sidelen ** 2-((sidelen/2) ** 2))
        self.jumpto(centerx - sidelen // 2,centery + height // 2) # // division and floor
        if fillme:
            self.t.begin_fill()
        for x in range(3):
            self.t.forward(sidelen)
            self.t.right(120)
        if fillme:
            self.t.end_fill()

    def hexagon(self, fillme,centerx, centery, sidelen):
        height = math.sqrt(sidelen ** 2-((sidelen/2) ** 2))
        self.jumpto(centerx-sidelen // 2,centery+height)
        if fillme:
            self.t.begin_fill()
        for x in range(6):
            self.t.forward(sidelen)
            self.t.right(60)
        if fillme:
            self.t.end_fill()

    # Star of David:
    def dstar(self, fillme,startx, starty, len):
        self.jumpto(startx - len // 2,starty + 0.2 * len)   # Estimate
        if fillme:
            self.t.begin_fill()
        for x in range(5):
            self.t.forward(len)
            self.t.right(144)
        if fillme:
            self.t.end_fill()

    def circle(self, fillme,centerx, centery, radius):
        self.jumpto(centerx,centery-radius)
        if fillme:
            self.t.begin_fill()
        self.t.circle(radius)
        if fillme:
            self.t.end_fill()
    
    def point(self, x, y, size):
        self.jumpto(x,y)
        self.t.dot(size)

    # Makes short lines around a circle with radius rad
    # and center point at (cx, cy). The parameter straylen
    # gives the length of each line, and color its color.
    # gap is an angle in decrees between the strays.
    def strays(self, cx, cy, rad, gap, straylen, color):
        self.setpensize(3)
        self.setcolor(color)
        self.setdir("up")
        gapindecrees = gap
        numboflines = int(360/gapindecrees)
        for i in range(numboflines):
            self.jumpto(cx,cy)
            self.t.right(gapindecrees)
            self.t.penup()
            self.t.forward(rad+10)
            self.t.pendown()
            self.t.forward(straylen)
        