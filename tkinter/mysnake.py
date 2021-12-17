import tkinter as tk
import random as rand
from tkinter import ttk

class App(tk.Tk):
    SIZE = 20
    COLOR_SNAKE = "yellow"
    DELAY = 200
    step = 1
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

    def on_array_press(self, event):
        if(event.keysym in ("Up", "Down","Left","Right")):
            self.dir = event.keysym

    def bind_keys(self):
        # Bind canvas with key events
        self.bind("<KeyPress>", self.on_array_press)
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
                    if (self.row > 0):
                        self.row -= self.app.step
                elif(self.app.dir == "Down"):
                    if (self.row < self.app.SIZE-1):
                        self.row += self.app.step
                elif(self.app.dir == "Left"):
                    if (self.col > 0):
                        self.col -= self.app.step
                else:
                    if (self.col < self.app.SIZE-1):
                        self.col += self.app.step

            # Show the snake:
            self.change_to(self.col, self.row, True)
            self.app.update()

    def run(self):
        while True:
            self.app.after(self.app.DELAY,self.take_step())



if __name__ == "__main__":
    app = App()
    app.mainloop()
