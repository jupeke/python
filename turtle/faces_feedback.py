import artist

class Face(artist.Artist):
    # Default values:
    bgcolor = "lightblue"
    pencolor = "green"
    fillcolor = "pink"
    pensize = 2
    penspeed = 0

    def __init__(self):
        # runs the init of the parent class:
        super().__init__(
            self.pencolor, 
            self.fillcolor, 
            self.pensize, 
            self.penspeed
        )
        self.screen.bgcolor(self.bgcolor)

    def reset(self):
        self.setcolor(self.pencolor)
        self.setfillcolor(self.fillcolor)
        self.setpensize(self.pensize)
        self.jumpto(0,0)
        self.setdir("right")

    def makeface(self, mode):
        # Clear old face
        self.t.clear()
        # Reset values
        self.reset()

        # Face
        self.circle(True, 0, 0, 300)
        
        # Eyes:
        cx1 = -100
        cx2 = 100
        cy = 100
        self.setcolor("darkgreen")
        self.circle(False, cx1, cy, 52)
        self.circle(False, cx2, cy, 52)
        self.setcolor("lightgreen")
        self.point(cx1, cy, 100)
        self.point(cx2, cy, 100)
        self.setcolor("black")
        self.point(cx1, cy, 30)
        self.point(cx2, cy, 30)

        # Strays around eyes.
        if (mode > 8):
            self.makestrays(cx1, cy, 52, 10, "yellow")
            self.makestrays(cx2, cy, 52, 10, "yellow")
        
        # Mouth:
        self.makemouth(mode, 0, -120)

        # Strays around the head.
        if (mode > 9):
            self.makestrays(0, 0, 330, 40, "red")
                
    # Creates a mouth with a starting point at the horizontal center.            
    def makemouth(self, grade, x, y):
        self.jumpto(x,y)
        self.setdir("right")
        self.setpensize(20)
        self.setcolor("red")
        numberofbits = int(grade/1.5)+10
        linelength = 19
        angle = grade-5
        x_var = x
        y_var = y
        for i in range(numberofbits):
            self.line(x_var, y_var, linelength)
            self.t.left(angle)
            x_var = self.getx()
            y_var = self.gety()
        
        self.jumpto(x,y)
        self.setdir("left")
        x_var = x
        y_var = y
        for i in range(numberofbits):
            self.line(x_var, y_var, linelength)
            self.t.right(angle)
            x_var = self.getx()
            y_var = self.gety()

    # Makes short lines around a circle with radius rad
    # center point at (cx, cy). The parameter straylen
    # gives the length of each line, and color its color.
    def makestrays(self, cx, cy, rad, straylen, color):
        self.setpensize(3)
        self.setcolor(color)
        self.setdir("up")
        gapindecrees = 40
        numboflines = int(360/gapindecrees)
        for i in range(numboflines):
            self.jumpto(cx,cy)
            self.t.right(gapindecrees)
            self.t.penup()
            self.t.forward(rad+10)
            self.t.pendown()
            self.t.forward(straylen)
       
f = Face()

# Listen to keyboard events: 
f.screen.listen()

# Bind key to methods. Note the cleve way to 
# pass an argument by using the lambda function.
# Hint found at https://www.codetoday.co.uk/post/how-to-pass-the-key-pressed-to-the-function-when-using-onkeypress-in-python-s-turtle-module
for n in range(1, 10):  # 1-9
    f.screen.onkeypress(lambda n=n: f.makeface(n), str(n))

# The 10 you get by pressing 0:
f.screen.onkeypress(lambda n=10: f.makeface(n), '0')
f.screen.onkeypress(f.t.clear, 'space')

# Prevent immediate exit:
f.donotautoexit()