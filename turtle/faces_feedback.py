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
        self.makemouth(mode, 0, -120)
                
    # Creates a mouth with a starting point at the horizontal center.            
    def makemouth(self, grade, x, y):
        self.jumpto(x,y)
        self.setdir("right")
        self.setpensize(20)
        self.setcolor("red")
        x_var = x
        y_var = y
        for i in range(int(grade/2)+10):
            self.line(x_var, y_var, 20)
            self.t.left(grade-5)
            x_var = self.getx()
            y_var = self.gety()
        
        self.jumpto(x,y)
        self.setdir("left")
        x_var = x
        y_var = y
        for i in range(int(grade/2)+10):
            self.line(x_var, y_var, 20)
            self.t.right(grade-5)
            x_var = self.getx()
            y_var = self.gety()

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