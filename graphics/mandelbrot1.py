from graphics import *
import cmath, math

MAX_COLOR = 256
WIN_WIDTH = 1000
WIN_HEIGHT = 1000
RATIO = 10 # unit step on screen = win_widht/ratio

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
        #self.draw_points()
        for p in self.points:
            p.get_mb_testpoints()
            #p.draw_testpoints()

        self.draw_mandelbrot_points()
        self.draw_not_mandelbrot_points()

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

        y_step = self.origin_y - WIN_WIDTH/RATIO # step length is the same.
        y1 = Line(Point(self.origin_x-2,y_step), \
            Point(self.origin_x+3,y_step))    # 1 is for line width
        y1.draw(win)
        label_y1 = Text(Point(self.origin_x+10,y_step), "1")
        label_y1.setSize(8)
        label_y1.draw(win)

        label_x = Text(Point(WIN_WIDTH-30, self.origin_y+10), 'x')
        label_x.draw(win)
        label_y = Text(Point(self.origin_x+10, 20), 'y')
        label_y.draw(win)

    def create_points(self):
        step = RATIO/WIN_WIDTH*4
        numb_of_points = 100
        for i in range(numb_of_points):
            x = -2+i*step
            for j in range(numb_of_points):
                y = -2+j*step
                p = ComplexPoint(complex(x,y),self.window)
                self.points.append(p)

    def draw_points(self):
        for p in self.points:
            p.draw_me(self.window, 'blue')

    def draw_mandelbrot_points(self):
        for p in self.points:
            if p.is_mb_point == True:
                p.draw_me(self.window, 'green')
    def draw_not_mandelbrot_points(self):
        for p in self.points:
            if p.is_mb_point == False:
                p.draw_me(self.window, 'red')

class ComplexPoint:
    MB_TEST_DEPTH = 50

    def __init__(self, cnumber, window):
        self.cnumber = cnumber
        self.x = cnumber.real
        self.y = cnumber.imag
        self.window = window
        self.mb_testpoints = []
        self.is_mb_point = False # Is a Mandelbrot point or not?

    # Draw the point to the window. The origin (0,0) is at the center of the window.
    def draw_me(self, win, color):
        p = self.get_point_object(win)
        p.setFill(color)
        p.draw(win)

    def draw_testpoints(self):
        for p in self.mb_testpoints:
            p.draw_me(self.window, 'red')

    def get_point_object(self, win):
        x_corrected = (WIN_WIDTH/RATIO)*self.x+WIN_WIDTH/2
        y_corrected = -(WIN_WIDTH/RATIO)*self.y+WIN_HEIGHT/2
        p = Point(x_corrected, y_corrected)
        return p

    # Return the modulus this complex number.
    def modulus(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        return r

    def get_mb_testpoints(self):
        self.is_mb_point = True # Default first
        testpoint = self.cnumber
        counter = 1
        for i in range(self.MB_TEST_DEPTH):
            cpoint = ComplexPoint(testpoint, self.window)
            if counter > 1:
                self.mb_testpoints.append(cpoint)

            # Test if is a Mandelbrot number:
            if self.is_mb_point==True and cpoint.modulus() > 2:
                self.is_mb_point = False

            # Counts the next one:
            testpoint = testpoint * testpoint + testpoint
            counter += 1


main = MainProgram()
main.run()
main.window.getMouse()# get mouse to click on screen to exit
main.window.close() # close the drawing window
