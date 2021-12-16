# based https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk
window = tk.Tk()
label = tk.Label(
    text="This is a label",
)
btn = tk.Button(
    text="click",
    #command = get_text
)
textfield = tk.Entry(width=50)
#label.grid(column=0,row=0,columnspan=3)

def get_text():
    global textfield
    global label
    txt = textfield.get()
    label.config(text=txt)

#btn.pack()
#label.pack()
#textfield.pack()

# grid geometry manager:
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            #relief=tk.RAISED,
            borderwidth=0
        )
        frame.grid(row=i, column=j+1)
        btn = tk.Button(master=frame, text=f"{i}{j}", width=5,height=2)
        btn.pack()


window.mainloop()
