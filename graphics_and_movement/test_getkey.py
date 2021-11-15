# Found at https://stackoverflow.com/questions/41156910/python-graphics-win-getkey-function
from graphics import *

win = GraphWin("My Test", 500, 500)

my_object = Circle(Point(50, 50), 10)

my_object.draw(win)

dx, dy = 10, 10

while True:
    k = win.checkKey()

    if k == 'Left':
        my_object.move(-dx, 0)
    elif k == 'Right':
        my_object.move(dx, 0)
    elif k == 'Down':
        my_object.move(0, dy)
    elif k == 'Up':
        my_object.move(0, -dy)

    # What's the name for space??
    elif k == 'KP_Space': # Not working!!
        my_object.move(0, -dy)
    elif k == 'period':
        break

win.close()
