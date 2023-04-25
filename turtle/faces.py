import artist

class Face(artist.Artist):
    # Default values:
    bgcolor = "lightblue"
    pencolor = "green"
    fillcolor = "pink"
    pensize = 2
    penspeed = 5

    def __init__(self, mode):
        # runs the init of the parent class:
        super().__init__(
            self.pencolor, 
            self.fillcolor, 
            self.pensize, 
            self.penspeed
        )
        self.mode = mode
        self.screen.bgcolor(self.bgcolor)
        self.makeface(self.mode)

    def makeface(self, mode):
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

f = Face("sad")         
f.screen.exitonclick()