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
        self.setcolor("darkgreen")
        self.circle(False, 100, 100, 52)
        self.circle(False, -100, 100, 52)
        self.setcolor("lightgreen")
        self.point(100, 100, 100)
        self.point(-100, 100, 100)
        self.setcolor("black")
        self.point(100, 100, 30)
        self.point(-100, 100, 30)

        # Mouth:
        if (mode == "happy"):
            self.t.right(60)
            x = -220
            y = 0
            self.setpensize(20)
            self.setcolor("red")
            for i in range(18):
                self.line(x, y, 30)
                self.t.left(7)
                x = self.getx()
                y = self.gety()

        elif (mode == "sad"):
            self.t.left(60)
            x = -220
            y = -150
            self.setpensize(20)
            self.setcolor("red")
            for i in range(18):
                self.line(x, y, 30)
                self.t.right(7)
                x = self.getx()
                y = self.gety()

        elif (mode == "neutral"):
            x = -220
            y = -50
            self.setpensize(20)
            self.setcolor("red")
            self.line(x, y, 440)
                


    def makehappyface(self):
        self.makeface("happy")
    def makesadface(self):
        self.makeface("sad")
    def makeneutralface(self):
        self.makeface("neutral")

f = Face()

# Listen to keyboard events: 
f.screen.listen()
# Bind key to methods:
f.screen.onkeypress(f.makesadface, 's')
f.screen.onkeypress(f.makehappyface, 'h')
f.screen.onkeypress(f.makeneutralface, 'n')
f.screen.onkeypress(f.t.clear, 'space')

# Prevent immediate exit:
f.turtle.mainloop()