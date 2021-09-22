from graphics import *

# Modified from the code at https://csveda.com/python-graphics-programming-using-graphics-py-module/
def main():
    colors=[]
    numb_of_circles = 5
    max=256
    red=max
    green=0
    blue=0
    difference = int(max/numb_of_circles)

    for i in range(numb_of_circles):
        red = int(red-difference)
        if red < 0:
            red = max
        colors.append(color_rgb(red,green,blue))

    win_width = 800
    win_height = 800
    window = GraphWin('Rainbow Circle', win_width, win_height) # give title and dimensions
    window.setBackground('black') # background color
    x_middle=window.getWidth()/2 # get x of middle of drawing area
    y_middle=window.getHeight()/2 # get y of middle of drawing area

    i=0
    while i<len(colors):
        gap = win_width/(numb_of_circles*2)
        cir=Circle(Point(x_middle, y_middle), 5+gap*i)# draw circle with center at middle of drawing area
        cir.setOutline(colors[i]) #get a next outline color from color array
        cir.setWidth(gap-5)#set outline width
        cir.draw(window)#draw the current circle
        i+=1 # increment counter for iteration

    message = Text(Point(x_middle, 50), 'Click to Exit')
    message.draw(window)
    window.getMouse()# get mouse to click on screen to exit
    window.close() # close the drawing window

main()
