# Found at https://stackoverflow.com/questions/41156910/python-graphics-win-getkey-function
from graphics import *
import time

win = GraphWin("My Test", 500, 500)
my_object = Circle(Point(50, 50), 10)
my_object.draw(win)
dx, dy = 1, 1

def moveme(obj, dir):
    go_on = True
    while go_on == True:
        if dir == "up":
            obj.move(0, -dy)
        elif dir == "down":
            obj.move(0, dy)
        elif dir == "left":
            obj.move(-dx, 0)
        else:
            obj.move(dx, 0)
        time.sleep(1)
        #if win.checkKey:
            #go_on = False

while True:
    k = win.checkKey()
    if k == 'Left':
        moveme(my_object, "left")
    elif k == 'Right':
        moveme(my_object, "right")
    elif k == 'Down':
        moveme(my_object, "down")
    elif k == 'Up':
        moveme(my_object, "up")

    elif k == 'period':
        break

win.close()
