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
        # Labels
        n1_lbl = ttk.Label(self, text="Number 1:")
        n1_lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        n2_lbl = ttk.Label(self, text="Number 2:")
        n2_lbl.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # Text fields
        n1_entry = ttk.Entry(self)
        n1_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        n2_entry = ttk.Entry(self)
        n2_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # Button
        mybutton = ttk.Button(self, text="Multiply", command=self.multiply)
        mybutton.grid(column=0, row=2, columnspan=2, sticky=tk.EW, padx=8, pady=8)

        # Label
        result_label = ttk.Label(self, text="Result: ")
        result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=10)

        widgets = [n1_lbl,n1_lbl, n1_entry,n2_entry,mybutton, result_label]
        return widgets

    def multiply(self):
        result = ""
        try:
            n1 = int(self.widgets[2].get())
            n2 = int(self.widgets[3].get())
            result = "{} x {} = {}".format(n1,n2,n1*n2)
        except ValueError:
            result = "Not an integer!"
        self.widgets[5].config(text=result)


if __name__ == "__main__":
    app = App()
    app.mainloop()
