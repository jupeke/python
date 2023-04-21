import artist
# Create instances of the Car class:
a = artist.Artist("green", "pink", 2, 5)
a.screen.bgcolor("lightblue")

# Face
a.circle(True, 0, 0, 300)

# Eyes:
a.setcolor("darkgreen")
a.circle(False, 100, 100, 52)
a.circle(False, -100, 100, 52)
a.setcolor("lightgreen")
a.point(100, 100, 100)
a.point(-100, 100, 100)
a.setcolor("black")
a.point(100, 100, 30)
a.point(-100, 100, 30)

# Mouth:
a.t.right(60)
x = -220
y = 0
a.setpensize(20)
a.setcolor("red")
for i in range(18):
    a.line(x, y, 30)
    a.t.left(7)
    x = a.getx()
    y = a.gety()

a.screen.exitonclick()