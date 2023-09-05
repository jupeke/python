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
t.goto(-200, -200)
t.pendown()

# Draw the main house
draw_square(400, "#C0C0C0")

# Draw the roof
t.penup()
t.goto(-200, 200)
t.pendown()
draw_triangle(400, "#A9A9A9")

# Draw the door
t.penup()
t.goto(-50, -200)
t.pendown()
draw_square(100, "#8B4513")

# Draw the window 1
t.penup()
t.goto(100, -100)
t.pendown()
draw_square(80, "#00CED1")

# Draw the window 2
t.penup()
t.goto(-220, -100)
t.pendown()
draw_square(80, "#00CED1")

# Draw the doorknob
t.penup()
t.goto(30, -180)
t.pendown()
draw_square(10, "#FFD700")

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.exitonclick()
