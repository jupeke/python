from graphics import *

def main():
    win_width = 800
    win_height = 800
    window = GraphWin('Circles', win_width, win_height) # give title and dimensions
    window.setBackground('black') # background color
    origin_x = window.getWidth()/2
    origin_y = window.getHeight()/2
    max_radius = window.getWidth()/2
    numb_of_circles = 20
    colors = make_colors(numb_of_circles)

    # Make the circles:
    circles = make_circles(colors, origin_x, origin_y, max_radius)

    # Draw the circles:
    for circle in circles:
        circle.draw(window)

    window.getMouse()# get mouse to click on screen to exit
    window.close() # close the drawing window

# Return a list with number colors
def make_colors(number):
    colors = []
    max = 256
    red = max
    green = 0
    blue = 0
    difference = int(max/number)
    for i in range(number):
        red = int(red-difference)
        if red < 0:
            red = 0
        colors.append(color_rgb(red,green,blue))
    return colors

# Return a list with circles, one in each color given in parameter 'colorw'.
def make_circles(colors, origin_x, origin_y, max_radius):
    circles = []
    i = 0
    radius = max_radius
    while i < len(colors):
        radius -= max_radius/len(colors) # Makes a bit smaller radius
        circle = Circle(Point(origin_x, origin_y), radius)
        circle.setFill(colors[i])
        circle.setOutline(colors[i])
        circles.append(circle)
        i += 1
    return circles

main()
