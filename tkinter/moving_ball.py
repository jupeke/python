# Based on https://www.tutorialspoint.com/moving-balls-in-tkinter-canvas
# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("800x600")

# Make the window size fixed
win.resizable(False,False)

# Create a canvas widget
canvas=Canvas(win, width=800, height=600)
canvas.pack()

# Create an oval or ball in the canvas widget
canvas.create_oval(20,20,40,40, fill="pink", tag="circle")

# https://stackoverflow.com/questions/47000765/tkinter-optimize-canvas-object-movement
canvas.create_oval(-10,-10,70,70, fill="", outline="", tag="circle")

# Move the ball
xspeed=yspeed=5

def move_ball():
   global xspeed, yspeed

   canvas.move("circle", 0, yspeed)
   (leftpos, toppos, rightpos, bottompos)=canvas.coords("circle")
   if leftpos <=0 or rightpos>=800:
      xspeed=-xspeed

   if toppos <=0 or bottompos >=600:
      yspeed=-yspeed

   canvas.after(20,move_ball)

canvas.after(20, move_ball)

win.mainloop()