import turtle
t = turtle
t.bgcolor("pink")

t.pen(pencolor="red", fillcolor="lightgreen", 
      pensize=2, speed=0)

t.penup()
t.bk(400)
t.pendown()

for i in range(180):    
    t.forward(600)
    t.right(182)
    t.penup()
    t.bk(100)
    t.pendown()

t.penup()
t.backward(200)
t.pendown()
t.Screen().exitonclick()