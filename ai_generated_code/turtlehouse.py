import turtle

# Create a turtle instance
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(10)

# Define function to draw a square
def draw_square(size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

# Define function to draw a triangle
def draw_triangle(size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Set the starting position of the turtle
t.penup()
t.goto(-150, -150)
t.pendown()

# Draw the main house
draw_square(200, "blue")

# Draw the roof
t.penup()
t.goto(-150, 50)
t.pendown()
draw_triangle(200, "red")

# Draw the door
t.penup()
t.goto(-50, -150)
t.pendown()
draw_square(50, "green")

# Draw the window
t.penup()
t.goto(75, -100)
t.pendown()
draw_square(50, "yellow")

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()
