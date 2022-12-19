import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x150")
        self.title('Multiply')
        self.resizable(0, 0)
        self.widgets = self.create_widgets()

    def create_widgets(self):
        # Labels
        

        # Text fields
        

        # Button
        

        # Label
        

        widgets = []
        return widgets

    def multiply(self):
        result = ""
        #try:
            #n1 = int(self.widgets[2].get())
            #n2 = int(self.widgets[3].get())
            #result = "{} x {} = {}".format(n1,n2,n1*n2)
        #except ValueError:
            #result = "Not an integer!"
        #self.widgets[5].config(text=result, background="pink")


if __name__ == "__main__":
    app = App()
    app.mainloop()
