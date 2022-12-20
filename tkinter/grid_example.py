import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.geometry("300x200")
        self.title("My title")
        self.widgets = self.create_widgets()

    def create_widgets(self):
        lbl = ttk.Label(self, text="Number 1:")
        lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # Text fields
        entry = ttk.Entry(self)
        entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        topframe = tk.Frame(self, bg='pink')
        topframe.grid(row=1,column=0, columnspan=2,sticky="s",pady=5) # Must be! (grid / pack / place)

        btn1 = tk.Button(topframe, text="1",width=2,height=1, command=self.dosomething())
        btn1.grid(row=0,column=0,padx=2,pady=2)
        btn2 = tk.Button(topframe, text="2",width=2,height=1)
        btn2.grid(row=0,column=1,padx=2,pady=2)

        bottomframe = tk.Frame(self, bg='green')
        bottomframe.grid(row=2,column=0, columnspan=2,pady=5) 
        result = tk.Label(bottomframe, text = "This is a label")
        result.grid(row=0,column=0,padx=2,pady=2)

        widgets = [topframe, bottomframe, result]
        return widgets

    def get_number(self):
        number = self.BAD_NUMBER
        try:
            number = int(self.widgets[2].get())
        except ValueError:
            pass
        return number

    def dosomething(self):
        result 
        self.widgets[2].config(text=result, background="pink")

if __name__ == "__main__":
    app = App()
    app.mainloop()
