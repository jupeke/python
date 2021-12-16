import tkinter as tk
import random as rand
from tkinter import ttk

class App(tk.Tk):
    SIZE = 20
    COLOR_SNAKE = "yellow"
    DELAY = 500
    step = 0
    dir = "none"

    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.title('My version of the famous Snake')
        self.resizable(0, 0)

        max = self.SIZE-1
        self.snake = Snake(rand.randint(0, max),rand.randint(0,max),self)
        self.widgets = self.create_widgets()
        self.bind_keys()
        self.snake.run()

    def create_widgets(self):
        widgets = []
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                color = "black"
                # Belongs to snake?
                if((i == self.snake.col) and (j == self.snake.row)):
                    color = self.COLOR_SNAKE
                # Label
                lbl = tk.Label(self,width=2,height=1,bg=color)
                lbl.grid(column=i, row=j, sticky=tk.SW)
                widgets.append(lbl)

        return widgets

    def go(self, dir):
        if(dir in ("Up", "Down","Left","Right")):
            self.dir = dir
        if(self.step == 0):
            self.step = 1

    def bind_keys(self):
        # Bind canvas with key events
        self.bind("<Up>", self.go("Up"))
        self.bind("<Down>", self.go("Down"))
        self.bind("<Left>", self.go("Left"))
        self.bind("<Right>", self.go("Right"))
        self.focus_set()

class Snake:
    # col and row begin from 0.
    def __init__(self, col, row, app):
        self.col = col
        self.row = row
        self.app = app

    # Set the label color to indicate snake or then not.
    def change_to(self, col, row, snake):
        if(snake == True):
            lbl_color = self.app.COLOR_SNAKE
        else:
            lbl_color = "black"
        lbl = tk.Label(self.app,width=2,height=1,bg=lbl_color)
        lbl.grid(column=col, row=row, sticky=tk.SW)

    def take_step(self):
        if self.app.step > 0:
            self.change_to(self.col, self.row, False)

            if(self.app.dir in ("Up", "Down","Left","Right")):
                if (self.app.dir == "Up"):
                    self.row -= self.app.step
                elif(self.app.dir == "Down"):
                    self.row += self.app.step
                elif(self.app.dir == "Left"):
                    self.col -= self.app.step
                else:
                    self.col += self.app.step

            # Show the snake:
            self.change_to(self.col, self.row, True)

    def run(self):
        while True:
            self.app.after(self.app.DELAY,self.take_step())



if __name__ == "__main__":
    app = App()
    app.mainloop()
