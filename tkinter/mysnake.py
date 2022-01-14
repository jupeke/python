# Traditionally: snake should not touch at all (not even corners).
# Make a nice end: show the length of snake.
import tkinter as tk
import random as rand
from tkinter import ttk
class App(tk.Tk):
    SIZE = 20
    COLOR_SNAKE = "yellow"
    COLOR_BG = "black"
    COLOR_APPLE = "red"
    DELAY = 200
    UNKNOWN ="unknown"
    step = 1
    apple_power = 3
    dir = "none"
    end = False

    def __init__(self):
        super().__init__()
        self.title('One more version of "Snake"')
        self.resizable(0, 0)
        max = self.SIZE-1
        self.snake = Snake(rand.randint(0, max),rand.randint(0,max),self)
        self.widgets = self.create_widgets()
        self.bind_keys()
        self.apple = Apple(self.apple_power,self)
        self.snake.run()

    def create_widgets(self):
        widgets = []
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                color = self.COLOR_BG
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

    def finish(self):
        self.end = True
        mytext = "The End! Snake length: {}".format(self.snake.len)
        lbl = ttk.Label(text=mytext)
        lbl.grid(column=0, row=0,  columnspan=10, rowspan=1, ipadx=5,ipady=5)

class Apple:
    # power == how many more squares you get while touching
    def __init__(self, power, app):
        self.power = power
        self.app = app
        self.col = app.UNKNOWN
        self.row = app.UNKNOWN
        self.show()

    def show(self):
        lbl_color = self.app.COLOR_APPLE
        max = self.app.SIZE-1
        self.col = rand.randint(0, max)
        self.row = rand.randint(0, max)
        lbl = tk.Label(self.app, width=2,height=1,bg=lbl_color)
        lbl.grid(column=self.col, row=self.row, sticky=tk.SW)
        self.app.update()

class Snake:
    # col and row begin from 0.
    def __init__(self, col, row, app):
        self.col = col # Head of snake
        self.row = row # Head of snake
        self.app = app
        self.len = 1
        # list of tuples (col,row) each indicating the location of a square.
        # The first square ("head") is not included in the list.
        self.tail = []

    # Set the label color to indicate snake or then not.
    def change_to(self, col, row, snake):
        if(snake == True):
            lbl_color = self.app.COLOR_SNAKE
        else:
            # If the snake is on an apple, the snake eats it and a new apple
            # appears elsewhere.
            lbl_color = self.app.COLOR_BG
            if(self.col == self.app.apple.col and self.row == self.app.apple.row):
                self.increase_len()
                self.app.apple_power += 2
                self.app.apple = Apple(self.app.apple_power,self.app)

        lbl = tk.Label(self.app,width=2,height=1,bg=lbl_color)
        lbl.grid(column=col, row=row, sticky=tk.SW)

    # Adds the item to the first position of the list, pushing back all the
    # old ones.
    def add_first(self, list, item):
        list.insert(0,item)

    # Test if snake head touches the tail (that will end the game)
    def head_touches_tail(self):
        touching = False
        for tuple in self.tail:
            if (tuple[0] == self.col and tuple[1] == self.row):
                touching = True
                break
        return touching

    # This is called always when the snake takes a step, before the
    # head coordinates are changed,
    def update_tail(self):
        # Add old head to the first of tail.
        self.add_first(self.tail,(self.col,self.row))

        # The last of tail is removed only if snake is not growing.
        if(len(self.tail) > self.len-1):
            # Change color of the old last (if exists):
            if (self.len > 1):
                last_tuple = self.tail[-1]
                self.change_to(last_tuple[0], last_tuple[1], False)
            # Remove the last of tail
            self.tail.pop()

    def take_step(self):
        if self.app.step > 0:
            # The color of old head is changed only if there is no tail.
            if(self.len == 1):
                self.change_to(self.col, self.row, False)

            if(self.app.dir in ("Up", "Down","Left","Right")):
                if (self.app.dir == "Up"):
                    if (self.row > 0):
                        self.update_tail()
                        self.row -= self.app.step
                    else:
                        self.app.finish()
                elif(self.app.dir == "Down"):
                    if (self.row < self.app.SIZE-1):
                        self.update_tail()
                        self.row += self.app.step
                    else:
                        self.app.finish()
                elif(self.app.dir == "Left"):
                    if (self.col > 0):
                        self.update_tail()
                        self.col -= self.app.step
                    else:
                        self.app.finish()
                else:
                    if (self.col < self.app.SIZE-1):
                        self.update_tail()
                        self.col += self.app.step
                    else:
                        self.app.finish()

            # Check if head touches the tail:
            if (self.app.snake.head_touches_tail()):
                self.app.finish()

            # Show the snake:
            self.change_to(self.col, self.row, True)
            self.app.update()

    def increase_len(self):
        self.len += self.app.apple.power;

    def run(self):
        while not self.app.end:
            self.app.after(self.app.DELAY,self.take_step())

if __name__ == "__main__":
    app = App()
    app.mainloop()
