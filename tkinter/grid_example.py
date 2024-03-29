import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    BAD_NUMBER = "bad_number"
    def __init__(self):
        super().__init__()
        #self.geometry("300x200")
        self.title("Myapp")
        self.widgets = self.create_widgets()

    def create_widgets(self):
        lbl = ttk.Label(self, text="Number 1:")
        lbl.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        # Text field
        entry = ttk.Entry(self)
        entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        buttonframe = tk.Frame(self, bg='pink')
        buttonframe.grid(row=1,column=0, columnspan=2,sticky="s",pady=5) # Must be! (grid / pack / place)

        btn1 = ttk.Button(buttonframe, text="Double", command=self.double)  # No parenthesis!
        btn1.grid(row=0,column=0,padx=2,pady=2)
        btn2 = ttk.Button(buttonframe, text="Triple",command=self.triple)
        btn2.grid(row=0,column=1,padx=2,pady=2)

        bottomframe = tk.Frame(self, bg='green')
        bottomframe.grid(row=2,column=0, columnspan=2,pady=5) 
        result = tk.Label(bottomframe, text = "This is a label")
        result.grid(row=0,column=0,padx=2,pady=2)

        widgets = [entry,buttonframe, bottomframe, result]
        return widgets

    def get_number(self):
        number = self.BAD_NUMBER
        try:
            number = int(self.widgets[0].get())
        except ValueError:
            pass
        return number

    def double(self):
        result = self.get_number()
        if result == self.BAD_NUMBER:
            self.error("Bad or missing number!")
        else:
            self.widgets[3].config(text=result*2, background="yellow")
    
    def triple(self):
        result = self.get_number()
        if result == self.BAD_NUMBER:
            self.error("Bad or missing number!")
        else:
            self.widgets[3].config(text=result*3, background="lightgreen")

    def error(self, message):
        self.widgets[3].config(text=message, background="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()
