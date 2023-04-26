import artist
# Create instances of the Car class:
a = artist.Artist("green", "pink", 2, 0)
a.screen.bgcolor("lightblue")

# Face
x = -300
y = 300
a.jumpto(x, y)
a.setdir("right")
for i in range(31):
    a.line(x, y, 600)
    y -= 20

x = -300
y = 300
a.jumpto(x, y)
a.setdir("down")
for i in range(31):
    a.line(x, y, 600)
    x += 20

a.screen.exitonclick()