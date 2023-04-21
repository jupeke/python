import artist
# Create instances of the Car class:
a = artist.Artist("black", "pink", 2, 8)
a.screen.bgcolor("white")
a.line(-400,0,800)
a.t.left(90)
a.line(0,-400,800)

# Numbers:
font=("Arial", 14, "normal", "bold")
a.t.setheading(0)
placex = -403
d = -10
for i in range(20):
    a.jumpto(placex,10)
    a.t.write(d)
    placex += 40
    d += 1

a.t.left(90)
placey = -407
d = -10
for i in range(20):
    a.jumpto(10,placey)
    a.t.write(d)
    placey += 40
    d += 1

# ticks x-axis:
a.t.setheading(-90)
placex = -400
placey = 5
for i in range(20):
    a.jumpto(placex, placey)
    a.line(placex, placey, 10)
    placex += 40
 
# ticks y-axis:
a.t.setheading(0)
placex = -5
placey = -400
for i in range(20):
    a.jumpto(placex,placey)
    a.line(placex, placey, 10)
    placey += 40

a.screen.exitonclick()