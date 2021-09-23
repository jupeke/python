from graphics import *

def main():
    max=256
    red=max
    green=0
    blue=0


    win_width = 800
    win_height = 800
    window = GraphWin('Mandelbrot', win_width, win_height) # give title and dimensions
    window.setBackground('white') # background color
    x_middle=window.getWidth()/2 # get x of middle of drawing area
    y_middle=window.getHeight()/2 # get y of middle of drawing area

    p=Point(x_middle, y_middle)
    p.draw(window)#draw the current circle

    message = Text(Point(x_middle, 50), 'Click to Exit')
    message.draw(window)
    window.getMouse()# get mouse to click on screen to exit
    window.close() # close the drawing window

main()