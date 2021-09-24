from graphics import *
import cmath

class MainProgram():
    MAX_COLOR = 256
    points = []
    def __init__(self):
        self.red = self.MAX_COLOR
        self.green = 0
        self.blue = 0
        self.win_width = 1000
        self.win_height = 1000
        self.window = GraphWin('Mandelbrot', self.win_width, self.win_height) # give title and dimensions
        self.window.setBackground('white') # background color
        self.origin_x = self.win_width/2
        self.origin_y = self.win_height/2
        #self.message = Text(Point(self.origin_x, 20), 'Click to Exit')
        #self.message.draw(self.window)

    def run(self):
        self.create_coordinates(self.window)
        self.create_points()
        self.draw_points()
        for p in self.points:
            p.get_mb_testpoints()
            p.draw_testpoints()

    def create_coordinates(self, win):
        y_axe = Line(Point(self.origin_x,0), Point(self.origin_x,self.win_height))
        y_axe.setArrow("first")
        y_axe.draw(win)
        x_axe = Line(Point(0,self.origin_y), Point(self.win_width,self.origin_y))
        x_axe.setArrow("last")
        x_axe.draw(win)
        label_x = Text(Point(self.win_width-30, self.origin_y+10), 'x')
        label_x.draw(win)
        label_y = Text(Point(self.origin_x+10, 20), 'y')
        label_y.draw(win)

    def create_points(self):
        p = ComplexPoint(complex(0,1),self.window)
        self.points.append(p)

    def draw_points(self):
        for p in self.points:
            p.draw_me(self.window)

class ComplexPoint:
    MB_TEST_DEPTH = 50
    is_mb_point = False # Is a Mandelbrot point or not?

    def __init__(self, cnumber, window):
        self.cnumber = cnumber
        self.x = cnumber.real
        self.y = cnumber.imag
        self.window = window
        self.mb_testpoints = []

    # Draw the point to the window. The origin (0,0) is at the center of the window.
    def draw_me(self, win):
        p = self.get_point_object(win)
        p.draw(win)

    def draw_testpoints(self):
        for p in self.mb_testpoints:
            p.draw_me(self.window)

    def get_point_object(self, win):
        x_corrected = self.x+win.getWidth()/2
        y_corrected = self.y+win.getWidth()/2
        p = Point(x_corrected, y_corrected)
        return p

    # Return the modulus this complex number.
    def modulus(self):
        r = (self.x ** 2 + self.y ** 2) ** 0.5
        return r

    def get_mb_testpoints(self):
        self.is_mandelbrot_point = True # Default first
        testpoint = self.cnumber
        for i in range(self.MB_TEST_DEPTH):
            cpoint = ComplexPoint(testpoint, self.window)
            self.mb_testpoints.append(cpoint)

            # Test if is a Mandelbrot number:
            if self.is_mandelbrot_point and self.modulus() > 2:
                self.is_mandelbrot_point = False

            # Counts the next one:
            testpoint = testpoint * testpoint + testpoint


main = MainProgram()
main.run()
main.window.getMouse()# get mouse to click on screen to exit
main.window.close() # close the drawing window