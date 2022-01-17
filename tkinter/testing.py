# based https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

frame1 = ttk.Frame(window)
frame2 = ttk.Frame(window)

label = tk.Label(
    frame1,
    text="This is a label",
)
btn = tk.Button(
    frame1,
    text="click",
    #command = get_text
)
textfield = tk.Entry(frame1,width=50)

# Set up the grid in frame1
label.grid(column=0,row=0)
btn.grid(column=1,row=0)
textfield.grid(column=2,row=0)

def get_text():
    global textfield
    global label
    txt = textfield.get()
    label.config(text=txt)

# grid geometry manager:
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=frame2,
            #relief=tk.RAISED,
            borderwidth=0
        )
        frame.grid(row=i, column=j+1)
        btn = tk.Button(master=frame, text=f"{i}{j}", width=5,height=2)
        btn.pack()

frame1.grid(column=0, row=0)
frame2.grid(column=0, row=1, sticky=tk.S)

window.mainloop()
