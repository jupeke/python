from graphics import *
import cmath, math

MAX_COLOR = 256
WIN_WIDTH = 1000
WIN_HEIGHT = 1000
RATIO = 100 # unit step on screen = win_widht/ratio

class MainProgram():
    points = []
    def __init__(self):
        self.red = MAX_COLOR
        self.green = 0
        self.blue = 0
        self.window = GraphWin('Mandelbrot', WIN_WIDTH, WIN_HEIGHT)
        self.window.setBackground('white') # background color
        self.origin_x = WIN_WIDTH/2
        self.origin_y = WIN_HEIGHT/2
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
        y_axe = Line(Point(self.origin_x,0), Point(self.origin_x, WIN_HEIGHT))
        y_axe.setArrow("first")
        y_axe.draw(win)
        x_axe = Line(Point(0,self.origin_y), Point(WIN_WIDTH,self.origin_y))
        x_axe.setArrow("last")
        x_axe.setWidth(1)
        x_axe.draw(win)

        x_step = self.origin_x + WIN_WIDTH/RATIO
        x1 = Line(Point(x_step,self.origin_y-2), \
            Point(x_step,self.origin_y+1+2))    # 1 is for line width
        x1.draw(win)
        label_x1 = Text(Point(x_step,self.origin_y+10), "1")
        label_x1.setSize(8)
        label_x1.draw(win)

        label_x = Text(Point(WIN_WIDTH-30, self.origin_y+10), 'x')
        label_x.draw(win)
        label_y = Text(Point(self.origin_x+10, 20), 'y')
        label_y.draw(win)

    def create_points(self):
        p = ComplexPoint(complex(1,1),self.window)
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
        p.setFill("red")
        p.draw(win)

    def draw_testpoints(self):
        for p in self.mb_testpoints:
            p.draw_me(self.window)

    def get_point_object(self, win):
        x_corrected = RATIO*self.x+WIN_WIDTH/2
        y_corrected = RATIO*self.y+WIN_HEIGHT/2
        p = Point(x_corrected, y_corrected)
        return p

    # Return the modulus this complex number.
    def modulus(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
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
