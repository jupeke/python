from graphics import *
import cmath, math

MAX_COLOR = 256
WIN_WIDTH = 1200
WIN_HEIGHT = 900
RATIO = 4 # unit step on screen = win_width/ratio
POINTS_TO_DRAW = 100    # Number of points to draw
class MainProgram():
    points = []
    def __init__(self):
        self.red = MAX_COLOR
        self.mb_test_depth = 50
        self.zoom_factor = 1
        self.green = 0
        self.blue = 0
        self.window = GraphWin('Mandelbrot', WIN_WIDTH, WIN_HEIGHT)
        self.window.autoflush=False # Default is true -> redraws after every point...
        self.window.setBackground('black') # background color
        self.origin_x = int(WIN_WIDTH/2+WIN_WIDTH/8)
        self.origin_y = int(WIN_HEIGHT/2)
        self.window.flush()

    def run(self, draw_mdpoints, draw_notmdpoints, draw_testpoints):
        self.create_coordinates(self.window)
        self.window.flush()
        self.create_points()

        # Only after testing we know which points are md points.
        for p in self.points:
            p.get_mb_testpoints(draw_testpoints)

        self.window.flush()

        if draw_mdpoints == True:
            self.draw_mandelbrot_points()
            self.window.flush()

        if draw_notmdpoints == True:
            self.draw_not_mandelbrot_points()
            self.window.flush()

    def create_coordinates(self, win):
        color = "#444"
        y_axe = Line(Point(self.origin_x,0), Point(self.origin_x, WIN_HEIGHT))
        y_axe.setArrow("first")
        y_axe.setFill(color)
        y_axe.draw(win)
        x_axe = Line(Point(0,self.origin_y), Point(WIN_WIDTH,self.origin_y))
        x_axe.setArrow("last")
        x_axe.setFill(color)
        x_axe.setWidth(1)
        x_axe.draw(win)

        x_step = self.origin_x + WIN_WIDTH/RATIO
        x1 = Line(Point(x_step,self.origin_y-2), \
            Point(x_step,self.origin_y+1+2))    # 1 is for line width
        x1.setFill(color)
        x1.draw(win)
        label_x1 = Text(Point(x_step,self.origin_y+10), "1")
        label_x1.setSize(8)
        label_x1.setFill(color)
        label_x1.draw(win)

        y_step = self.origin_y - WIN_WIDTH/RATIO # step length is the same.
        y1 = Line(Point(self.origin_x-2,y_step), \
            Point(self.origin_x+3,y_step))    # 1 is for line width
        y1.setFill(color)
        y1.draw(win)
        label_y1 = Text(Point(self.origin_x+10,y_step), "1")
        label_y1.setSize(8)
        label_y1.setFill(color)
        label_y1.draw(win)

        label_x = Text(Point(WIN_WIDTH-30, self.origin_y+10), 'x')
        label_x.setFill(color)
        label_x.draw(win)
        label_y = Text(Point(self.origin_x+10, 20), 'y')
        label_y.setFill(color)
        label_y.draw(win)

    def create_points(self):
        step = RATIO/WIN_WIDTH*(1000/(POINTS_TO_DRAW*self.zoom_factor)) # The real distance between two points (x or y)

        # Idea: to cover equal distance on both sides of the origin:
        points_on_unit = 1/step
        x_start = self.origin_x - POINTS_TO_DRAW*points_on_unit/2
        y_start = self.origin_y - POINTS_TO_DRAW*points_on_unit/2

        for i in range(POINTS_TO_DRAW):
            x = x_start+i*step
            for j in range(POINTS_TO_DRAW):
                y = y_start+j*step
                p = ComplexPoint(complex(x,y),self)
                self.points.append(p)

    def draw_points(self):
        for p in self.points:
            p.draw_me(self.window, 'blue')

    def draw_mandelbrot_points(self):
        for p in self.points:
            if p.is_mb_point == True:
                p.draw_me(self.window, 'white')

    def draw_not_mandelbrot_points(self):
        for p in self.points:
            if p.is_mb_point == False:
                blue = 0
                green = 0
                esc = p.escape_threshold
                tdepth = self.mb_test_depth
                red = int(max(MAX_COLOR - ((esc*3)/tdepth)*MAX_COLOR, 0))
                color = color_rgb(red,green,blue)
                p.draw_me(self.window, color)

class ComplexPoint:
    def __init__(self, cnumber, main):
        self.cnumber = cnumber
        self.x = cnumber.real
        self.y = cnumber.imag
        self.main = main
        self.window = self.main.window
        self.is_mb_point = False # Is a Mandelbrot point or not?

        # Gives the number of test iterations needed to quit
        # the defined circle (-> hajaantuu)
        self.escape_threshold = 0 # 0 for md elements.

    # Draw the point to the window.
    def draw_me(self, win, color):
        p = self.get_point_object(win)
        p.setFill(color)
        p.draw(win)

    # Point on the screen:
    def get_point_object(self, win):
        x_corrected = (WIN_WIDTH/RATIO)*self.x+self.main.origin_x
        y_corrected = -(WIN_WIDTH/RATIO)*self.y+self.main.origin_y
        p = Point(x_corrected, y_corrected)
        return p

    # Return the modulus of this complex number.
    def modulus(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        return r

    def get_mb_testpoints(self,draw):
        self.is_mb_point = True # Default first
        testpoint = self.cnumber
        for i in range(self.main.mb_test_depth):
            cpoint = ComplexPoint(testpoint, self.main)

            # Test if is a Mandelbrot number. The limit
            # is 2 but with a big number we get more testpoints:
            if self.is_mb_point==True and cpoint.modulus() > 100:
                self.is_mb_point = False
                self.escape_threshold = int(i+1)
                break

            if draw == True and i > 0:
                cpoint.draw_me(self.window, 'red')

            # Counts the next one:
            testpoint = testpoint * testpoint + self.cnumber

main = MainProgram()
draw_mdpoints = True
draw_notmdpoints = True
draw_testpoints = False
main.run(draw_mdpoints, draw_notmdpoints, draw_testpoints)
main.window.getMouse()# get mouse to click on screen to exit
main.window.close() # close the drawing window
