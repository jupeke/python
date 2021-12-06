import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #self.geometry("240x100")
        self.title('My window')
        self.resizable(0, 0)
        self.widgets = self.create_widgets()

    def create_widgets(self):
        # Label
        name_label = ttk.Label(self, text="Name:")
        name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        # Text field
        name_entry = ttk.Entry(self)
        name_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # Button
        mybutton = ttk.Button(self, text="Click me", command=self.greet)
        mybutton.grid(column=0, row=1, columnspan=2, padx=8, pady=8)

        # Label
        result_label = ttk.Label(self, text="Result")
        result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=10)

        widgets = [name_label,name_entry,mybutton, result_label]
        return widgets

    def greet(self):
        txt = self.widgets[1].get()
        self.widgets[3].config(text="Hello "+txt)


if __name__ == "__main__":
    app = App()
    app.mainloop()
