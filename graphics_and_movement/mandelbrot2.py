from graphics import *
import cmath, math

MAX_COLOR = 255
WIN_WIDTH = 800
WIN_HEIGHT = 800
RATIO = 4 # unit step on screen in pxs = win_width/ratio * zoom_factor
POINTS_TO_DRAW = 500    # Number of points to draw
class MainProgram():
    points = []
    def __init__(self):
        self.red = MAX_COLOR
        self.mb_test_depth = 255
        self.zoom_factor = 1
        self.green = 0
        self.blue = 0
        self.window = GraphWin('Mandelbrot', WIN_WIDTH, WIN_HEIGHT)
        self.window.autoflush=False # Default is true -> redraws after every point...
        self.window.setBackground('black') # background color
        self.focus_x = -0.5 # Center of the testpoints (x) = the center point!
        self.focus_y = 0 # Center of the testpoints (y) = the center point!
        self.center_x_in_px = int(WIN_WIDTH/2)
        self.center_y_in_px = int(WIN_HEIGHT/2)
        self.origin_x_in_px = self.get_origin_x_in_px()
        self.origin_y_in_px = self.get_origin_y_in_px()
        self.window.flush()

    # Converts a number of pixels (mouse) into custom coordinate units
    # (unit = length of [0,1] on the screen)
    def pixels_to_units(self, px):
        # Length of interval [0,1] in pixels
        len_unit_on_screen_px = self.zoom_factor * WIN_WIDTH / RATIO
        return px / len_unit_on_screen_px

    # Converts coordinate units (unit = length of [0,1] on the screen) into the number of pixels
    def units_to_pixels(self, len):
        # Length of interval [0,1] in pixels
        len_unit_on_screen_px = self.zoom_factor * WIN_WIDTH / RATIO
        return len * len_unit_on_screen_px

    # Converts the position coordinate of x in pixels into real coordinate value.
    def position_x_to_coordinate_x(self, x_pos):
        distance_from_origin_x_in_px = x_pos - self.origin_x_in_px
        return self.pixels_to_units(distance_from_origin_x_in_px)

    # Converts the position coordinate of y in pixels into real coordinate value.
    def position_y_to_coordinate_y(self, y_pos):
        distance_from_origin_y_in_px = self.origin_y_in_px-y_pos
        return self.pixels_to_units(distance_from_origin_y_in_px)

     # Converts the real coordinate value to window position coordinate of y.
    def coordinate_x_to_position_x(self, x):
        return self.origin_x_in_px + self.units_to_pixels(x)

    # Converts the real coordinate value to window position coordinate of y.
    def coordinate_y_to_position_y(self, y):
        return self.origin_y_in_px - self.units_to_pixels(y)

    def get_origin_x_in_px(self):
        return self.center_x_in_px + self.units_to_pixels(-self.focus_x)

    def get_origin_y_in_px(self):
        return self.center_y_in_px - self.units_to_pixels(-self.focus_y)

    def update_origin(self):
        self.origin_x_in_px = self.get_origin_x_in_px()
        self.origin_y_in_px = self.get_origin_y_in_px()

    def set_title(self, new):
        self.window.setTitle(new)

    # Converts the position coordinate of focus x in pixels into real coordinate value.
    def focus_pos_x_to_coordinate_x(self, focus_pos_x):
        asdf

    # Converts the position coordinate of focus y in pixels into real coordinate value.
    def focus_pos_y_to_coordinate_y(self, focus_pos_y):
        asdf

    # Found at https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
    def clear(self, win):
        for item in win.items[:]:
            item.undraw()
        win.update()

    def show(self, focus_pos, zoom, draw_mdpoints, draw_notmdpoints, draw_testpoints):
        self.set_title("Mandelbrot: zoom_factor = {}".format(zoom))
        self.points = []
        self.focus_x = self.position_x_to_coordinate_x(focus_pos.x)
        self.focus_y = self.position_y_to_coordinate_y(focus_pos.y)
        self.zoom_factor = zoom
        self.update_origin()
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
        y_axe = Line(Point(self.origin_x_in_px,0), Point(self.origin_x_in_px, WIN_HEIGHT))
        y_axe.setArrow("first")
        y_axe.setFill(color)
        y_axe.draw(win)
        x_axe = Line(Point(0,self.origin_y_in_px), Point(WIN_WIDTH,self.origin_y_in_px))
        x_axe.setArrow("last")
        x_axe.setFill(color)
        x_axe.setWidth(1)
        x_axe.draw(win)

        x_step = self.coordinate_x_to_position_x(1)
        x1 = Line(Point(x_step,self.origin_y_in_px-2), \
            Point(x_step,self.origin_y_in_px+1+2))    # 1 is for line width
        x1.setFill(color)
        x1.draw(win)
        label_x1 = Text(Point(x_step,self.origin_y_in_px+10), "1")
        label_x1.setSize(8)
        label_x1.setFill(color)
        label_x1.draw(win)

        y_step = self.coordinate_y_to_position_y(1)
        y1 = Line(Point(self.origin_x_in_px-2,y_step), \
            Point(self.origin_x_in_px+3,y_step))    # 1 is for line width
        y1.setFill(color)
        y1.draw(win)
        label_y1 = Text(Point(self.origin_x_in_px+10,y_step), "1")
        label_y1.setSize(8)
        label_y1.setFill(color)
        label_y1.draw(win)

        label_x = Text(Point(WIN_WIDTH-30, self.origin_y_in_px+10), 'x')
        label_x.setFill(color)
        label_x.draw(win)
        label_y = Text(Point(self.origin_x_in_px+10, 20), 'y')
        label_y.setFill(color)
        label_y.draw(win)

    def create_points(self):
        # Idea: the test points fill always the whole window (a square).
        step_in_px = WIN_WIDTH/POINTS_TO_DRAW # The number line distance between two points (x or y)
        step_in_units = self.pixels_to_units(step_in_px)

        # Idea: to cover equal distance on both sides of the focus:
        x_start =  self.focus_x- 0.5 * POINTS_TO_DRAW * step_in_units
        y_start =  self.focus_y- 0.5 * POINTS_TO_DRAW * step_in_units

        for i in range(POINTS_TO_DRAW):
            x = x_start+i*step_in_units
            for j in range(POINTS_TO_DRAW):
                y = y_start+j*step_in_units
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
                #red = int(max(MAX_COLOR - ((esc*3)/tdepth)*MAX_COLOR, 0))
                #red = int(min(((esc*1)/tdepth)*MAX_COLOR, MAX_COLOR))
                red = MAX_COLOR % esc
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
        x_corrected = main.coordinate_x_to_position_x(self.x)
        y_corrected = main.coordinate_y_to_position_y(self.y)
        p = Point(x_corrected, y_corrected)
        return p

    # Return the modulus of this complex number.
    def modulus(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        return r

    def get_mb_testpoints(self,draw):
        self.is_mb_point = True # Default first
        testpoint = self.cnumber
        limit = 100
        for i in range(self.main.mb_test_depth):
            cpoint = ComplexPoint(testpoint, self.main)

            # Test if is a Mandelbrot number. The limit
            # is 2 but with a big number we get more testpoints:
            if self.is_mb_point==True and cpoint.modulus() > limit:
                self.is_mb_point = False
                self.escape_threshold = int(i+1)
                break

            if draw == True and i > 0:
                cpoint.draw_me(self.window, 'red')

            # Counts the next one:
            testpoint = testpoint * testpoint + self.cnumber

main = MainProgram()
i = 0
focus = Point(WIN_WIDTH/2,WIN_WIDTH/2)
draw_mdpoints = True
draw_notmdpoints = True
draw_testpoints = False
zoom = 1
while True:
    '''
    # Did the user click the window close button?
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Direction?
            if event.key == K_DOWN:
                running = False
        if event.type == pygame.QUIT:
            running = False
    '''
    main.show(focus, zoom, draw_mdpoints, draw_notmdpoints, draw_testpoints)
    key_pressed = main.window.checkKey()
    if key_pressed == 'Up':
        zoom = zoom * 100
        #main.clear(main.window)
        #main.show(focus, zoom, draw_mdpoints, draw_notmdpoints, draw_testpoints)
    elif key_pressed == 'Down':
        zoom = zoom / 100
        #main.clear(main.window)
        #main.show(focus, zoom, draw_mdpoints, draw_notmdpoints, draw_testpoints)'''

    focus = main.window.getMouse()
    main.clear(main.window)

main.window.getMouse()
main.window.close() # close the drawing window
