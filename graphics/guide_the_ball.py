# Found at https://stackoverflow.com/questions/41156910/python-graphics-win-getkey-function
from graphics import *
import time

win = GraphWin("My Test", 500, 500)
my_object = Circle(Point(50, 50), 10)
my_object.setFill("white")
my_object.draw(win) # Draws the window

DELAY = 0.02
step = 1
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

    moveme(my_object, direction, step)
    time.sleep(DELAY)

win.close()
