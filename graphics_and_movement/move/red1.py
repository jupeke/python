import sys,time, math, random

# setting path to be able to import from parent folder:
'''sys.path.append('..graphics_and_movement')
from graphics_and_movement.graphics import * Should work but does not...'''
from graphics import *

WINSIZE = 500
win = GraphWin("My Test", WINSIZE, WINSIZE)
me = Circle(Point(50, 50), 10)
me.setFill("white")
red = Circle(Point(int(random.random()*WINSIZE), WINSIZE), 10)
red.setFill("red")
me.draw(win)
red.draw(win)

DELAY = 0.02
step = 3
step_enemy = 2
direction = "Right"
dir_enemy = "Up"

def dist_circles(circle1, circle2):
    r1 = circle1.radius
    cx1 = circle1.getCenter().x
    cy1 = circle1.getCenter().y

    r2 = circle2.radius
    cx2 = circle2.getCenter().x
    cy2 = circle2.getCenter().y


    dist_centers = math.sqrt(pow(cx1-cx2,2)+pow(cy1-cy2,2))
    #dist_centers_tothe2 = pow(cx1-cx2,2)+pow(cy1-cy2,2)
    dist_final = dist_centers-(r1+r2)
    return dist_final
    #return dist_centers_tothe2

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
    r = me.radius
    center = me.getCenter()
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

    moveme(me, direction, step)
    movered(red, dir_enemy, step_enemy)
    if(dist_circles(me, red) < 0):
        step = 0
        step_enemy = 0
    time.sleep(DELAY)

win.close()
