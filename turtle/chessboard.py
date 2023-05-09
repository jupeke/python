import artist

a = artist.Artist("black", "black", 1, 0)
a.screen.bgcolor("#cccccc")
sidelen = 80
rowbeginwhite = True
startx = -(4*sidelen-int(sidelen/2))
starty = 4*sidelen-int(sidelen/2)
y = starty
for i in range(8):
    x = startx
    rowwhite = rowbeginwhite
    for k in range(8):
        if (rowwhite):
            fillcol = "white"
            rowwhite = False
        else:
            fillcol = "black"
            rowwhite = True
        a.t.fillcolor(fillcol)
        a.square(True, x, y, sidelen)
        x += sidelen
    y -= sidelen    
    if(rowbeginwhite):
        rowbeginwhite = False
    else:
        rowbeginwhite = True

a.t.hideturtle()
a.donotautoexit()