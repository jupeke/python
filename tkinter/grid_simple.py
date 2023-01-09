import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Myapp")
        self.widgets = self.create_widgets()

    def create_widgets(self):
        # Label for the text field:
        lbl = ttk.Label(self, text="Name: ")
        lbl.grid(column=0, row=0, sticky="w", padx=5, pady=5)

        # Text field:
        entry = ttk.Entry(self)
        entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # Button:
        btn1 = ttk.Button(self, text="click", command=self.greet)  # No parenthesis!
        btn1.grid(row=1,column=0,padx=2,pady=2)

        # Label for the message:
        lbl2 = ttk.Label(self)
        lbl2.grid(column=1,row=1)

        widgets = [lbl, entry, lbl2]
        return widgets

    def greet(self):
        name = self.widgets[1].get()
        self.widgets[2].config(text="Hello "+name, background="yellow")

if __name__ == "__main__":
    app = App()
    app.mainloop()
