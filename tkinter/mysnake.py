import tkinter as tk
import random as rand
from tkinter import ttk

class App(tk.Tk):
    SIZE = 20
    COLOR_SNAKE = "yellow"
    STEP = 0

    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.title('My version of the famous Snake')
        self.resizable(0, 0)

        max = self.SIZE-1
        self.snake = Snake(rand.randint(0, max),rand.randint(0,max))
        self.widgets = self.create_widgets()

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
                lbl.grid(column=i, row=j, sticky=tk.W)
                widgets.append(lbl)

        return widgets

    def move(self, dir):
        

    def greet(self):
        # Bind canvas with key events
        self.bind("<Up>", self.move("up"))
        self.bind("<Down>", self.move("down"))
        self.bind("<Left>", self.move("left"))
        self.bind("<Right>", self.move("right"))
        self.focus_set()

class Snake:
    # col and row begin from 0.
    def __init__(self, col, row):
        self.col = col
        self.row = row
    #def show(self):


if __name__ == "__main__":
    app = App()
    app.mainloop()
