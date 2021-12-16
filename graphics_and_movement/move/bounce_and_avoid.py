import sys

# setting path to be able to import from parent folder:
'''sys.path.append('..graphics_and_movement')
from graphics_and_movement.graphics import * Should work but does not...'''
from graphics import *
import time

WINSIZE = 500
win = GraphWin("My Test", WINSIZE, WINSIZE)
my_object = Circle(Point(50, 50), 10)
my_object.setFill("white")
my_object.draw(win) # Draws the window

DELAY = 0.02
step = 3
direction = "Right"

# Moves obj one step (pxls) to direction dir
def moveme(obj, dir, step):
    if dir == "Up":
        obj.move(0, -step)  # redraws the window, too.
    elif dir == "Down":
        obj.move(0, step)
    elif dir == "Left":
        obj.move(-step, 0)
    elif dir == "Right":
        obj.move(step, 0)

# Main loop:
while True:
    k = win.checkKey()
    if k in ("Up", "Down","Left","Right"):
        direction = k

    # Bounce from the walls.
    r = my_object.radius
    center = my_object.getCenter()
    if center.x > WINSIZE-r:
        direction = "Left"
    elif center.x < 0+r:
        direction = "Right"
    elif center.y > WINSIZE-r:
        direction = "Up"
    elif center.y < 0+r:
        direction = "Down"

    moveme(my_object, direction, step)
    time.sleep(DELAY)

win.close()
