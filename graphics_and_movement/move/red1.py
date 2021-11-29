import sys

# setting path to be able to import from parent folder:
'''sys.path.append('..graphics_and_movement')
from graphics_and_movement.graphics import * Should work but does not...'''
from graphics import *
import time
import random

WINSIZE = 500
win = GraphWin("My Test", WINSIZE, WINSIZE)
my_object = Circle(Point(50, 50), 10)
my_object.setFill("white")
red = Circle(Point(int(random.random()*WINSIZE), 50), 10)
red.setFill("red")
my_object.draw(win)
red.draw(win)

DELAY = 0.02
step = 3
step_enemy = 2
direction = "Right"
dir_enemy = "Up"

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

# Moves obj one step (pxls) to direction dir
def movered(obj, dir, step):
    if dir == "Up":
        obj.move(0, -step)  # redraws the window, too.
    elif dir == "Down":
        obj.move(0, step)

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

    # The red enemy:
    r_red = red.radius
    center_enemy = red.getCenter()

    if center_enemy.y > WINSIZE-r_red:
        dir_enemy = "Up"
    elif center_enemy.y < 0+r_red:
        dir_enemy = "Down"

    moveme(my_object, direction, step)
    movered(red, dir_enemy, step_enemy)
    time.sleep(DELAY)

win.close()
