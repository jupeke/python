import artist
# Create instances of the Car class:
a = artist.Artist("green", "pink", 2, 5)
a.screen.bgcolor("lightblue")

a.circle(True, 0, 0, 300)
a.point(100, 100, 100)
a.point(-100, 100, 100)
a.t.right(60)
x = -100
y = 0
for i in range(10):
    a.line(-100, 0, 50)
    a.t.left(12)

a.screen.exitonclick()