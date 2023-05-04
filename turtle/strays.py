import artist

class Art(artist.Artist):
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
        self.paint()

    def reset(self):
        self.setcolor(self.pencolor)
        self.setfillcolor(self.fillcolor)
        self.setpensize(self.pensize)
        self.jumpto(0,0)
        self.setdir("right")

    def paint(self):
        self.strays(0, 0, 10, 5, 300,"red")
    
       
f = Art()



# Prevent immediate exit:
f.donotautoexit()