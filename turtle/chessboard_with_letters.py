import artist

a = artist.Artist("black", "black", 1, 0)
a.screen.bgcolor("#cccccc")
sidelen = 80
rowbeginwhite = True
startx = -(4*sidelen-int(sidelen/2))
starty = 4*sidelen-int(sidelen/2)
letters = ["a","b","c","d","e","f","g","h"]
size = 8
#if (size > 8):

# Write the numbers and letters above and on the left
x = startx
y = starty
for i in range(size):
    a.jumpto(x, int(y+sidelen*0.6))
    fontsize = int(sidelen/5)
    a.t.write(letters[i], align="center",
              font=("Verdana",fontsize, "bold"))
    x += sidelen

x = startx
y = starty
for i in range(size):
    a.jumpto(int(x-sidelen*0.8), int(y-sidelen*0.15))
    fontsize = int(sidelen/5)
    a.t.write(str(size-i), align="center",
              font=("Verdana",fontsize, "bold"))
    y -= sidelen

y = starty
for i in range(size):
    x = startx
    rowwhite = rowbeginwhite
    for k in range(size):
        if (rowwhite):
            fillcol = "white"
            textcol = "black"
            rowwhite = False
        else:
            fillcol = "black"
            textcol = "white"
            rowwhite = True
        a.t.fillcolor(fillcol)
        a.square(True, x, y, sidelen)
        a.t.pencolor(textcol)
        a.jumpto(x, int(y-sidelen*0.1))
        text = letters[k]+str(size-k)
        fontsize = int(sidelen/7)
        a.t.write(text, align="center",
                  font=("Verdana",fontsize, "normal"))
        a.jumpto(x,y)
        a.t.pencolor("black")
        x += sidelen
    y -= sidelen    
    if(rowbeginwhite):
        rowbeginwhite = False
    else:
        rowbeginwhite = True

a.t.hideturtle()
a.donotautoexit()