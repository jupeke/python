from graphics import *
import cmath

class MainProgram():
    MAX_COLOR = 256
    points = []
    def __init__(self):
        self.red = self.MAX_COLOR
        self.green = 0
        self.blue = 0
        self.win_width = 800
        self.win_height = 800
        self.window = GraphWin('Mandelbrot', self.win_width, self.win_height) # give title and dimensions
        self.window.setBackground('white') # background color
        self.message = Text(Point(self.win_width/2, 20), 'Click to Exit')
        self.message.draw(self.window)

    def run(self):
        self.create_points()
        self.draw_points()

    def create_points(self):
        p = ComplexPoint(complex(100,100))
        self.points.append(p)

    def draw_points(self):
        for p in self.points:
            p.draw_me(self.window)

class ComplexPoint:
    MB_TEST_DEPTH = 100
    def __init__(self, cnumber):
        self.cnumber = cnumber
        self.x = cnumber.real
        self.y = cnumber.imag
        self.mb_test_points = []

    # Draw the point to the window. The origin (0,0) is at the center of the window.
    def draw_me(self, win):
        p = self.get_point_object(win)
        p.draw(win)

    def get_point_object(self, win):
        x_corrected = self.x+win.getWidth()/2
        y_corrected = self.y+win.getWidth()/2
        p = Point(x_corrected, y_corrected)
        return p

    def modulus(self):
        r = self.x jakta

    def is_mandelbrot_point(self):
        jkljöj
    def get_mb_test_points(self):
        testpoint = self.cnumber
        for i in range(MB_TEST_DEPTH):
            self.mb_test_points.append(testpoint)

            # Counts the next one:
            testpoint = testpoint*testpoint + testpoint


main = MainProgram()
main.run()
main.window.getMouse()# get mouse to click on screen to exit
main.window.close() # close the drawing window