import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    BAD_NUMBER = "bad_number"
    def __init__(self):
        super().__init__()
        #self.geometry("220x100")
        self.title('Multiply')
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

        # Buttons. Note that ttk.Button does not support width / height.
        '''mybutton = ttk.Button(self, text="+", command=self.add)
        mybutton.grid(column=0, row=2, columnspan=1, sticky=tk.W, padx=0, pady=0)
        mybutton = ttk.Button(self, text="-", command=self.subtract)
        mybutton.grid(column=0, row=2, columnspan=1, sticky=tk.E, padx=0, pady=0)
        mybutton = ttk.Button(self, text="*", command=self.multiply)
        mybutton.grid(column=0, row=3, columnspan=1, sticky=tk.W, padx=0, pady=0)
        mybutton = ttk.Button(self, text="/", command=self.divide)
        mybutton.grid(column=0, row=3, columnspan=1, sticky=tk.E, padx=0, pady=0)
        '''
        btn_frame = tk.Frame(self, bg='pink')

        plusbutton = tk.Button(btn_frame, text="+", width=2,height=1, command=self.add)
        plusbutton.grid(row=0, column=0, padx=0, pady=0) # btn_frame has its own grid.
        minusbutton = tk.Button(btn_frame, text="-", width=2,height=1, command=self.subtract)
        minusbutton.grid(row=0, column=1, padx=0, pady=0)
        timesbutton = tk.Button(btn_frame, text="*", width=2,height=1, command=self.multiply)
        timesbutton.grid(row=1, column=0, padx=0, pady=0)
        dividebutton = tk.Button(btn_frame, text="/", width=2,height=1, command=self.divide)
        dividebutton.grid(row=1, column=1, padx=0, pady=0)
        
        # Set the frame into the main grid:
        btn_frame.grid(column=0, row=3, columnspan=2, sticky=tk.S, padx=5, pady=5)

        # Label
        result_label = ttk.Label(self, text="Result will be shown here")
        result_label.grid(column=0, row=4, columnspan=2, padx=5, pady=10)

        widgets = [n1_lbl,n1_lbl, n1_entry,n2_entry,btn_frame, result_label]
        return widgets
    #
    def get_numbers(self):
        numbers = [self.BAD_NUMBER, self.BAD_NUMBER]
        try:
            numbers[0] = int(self.widgets[2].get())
            numbers[1] = int(self.widgets[3].get())
        except ValueError:
            pass
        return numbers


    def multiply(self):
        numbers = self.get_numbers()
        if self.BAD_NUMBER in numbers:
            result = "Bad or missing number!"
        else:
            result = "{} x {} = {}".format(numbers[0],numbers[1],numbers[0]*numbers[1])
        self.widgets[5].config(text=result, background="pink")
    def add(self):
        numbers = self.get_numbers()
        if self.BAD_NUMBER in numbers:
            result = "Bad or missing number!"
        else:
            result = "{} + {} = {}".format(numbers[0],numbers[1],numbers[0]+numbers[1])
        self.widgets[5].config(text=result, background="green")
    def subtract(self):
        numbers = self.get_numbers()
        if self.BAD_NUMBER in numbers:
            result = "Bad or missing number!"
        else:
            result = "{} - {} = {}".format(numbers[0],numbers[1],numbers[0]-numbers[1])
        self.widgets[5].config(text=result, background="lightblue")
    def divide(self):
        numbers = self.get_numbers()
        if self.BAD_NUMBER in numbers:
            result = "Bad or missing number!"
        else:
            result = "{} : {} = {}".format(numbers[0],numbers[1],numbers[0]/numbers[1])
        self.widgets[5].config(text=result, background="yellow")

if __name__ == "__main__":
    app = App()
    app.mainloop()
