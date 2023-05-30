import turtle

turtle.bgcolor("pink")

def make_square(size, pencolor, fillcolor):
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.pensize(size)

    turtle.begin_fill()
    for i in range(4):
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()

make_square(20, "red", "blue")


turtle. Screen(). exitonclick()