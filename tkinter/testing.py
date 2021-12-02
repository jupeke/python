# based https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
import tkinter as tk
window = tk.Tk()
frame_start = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_start.grid(column=0,row=0,columnspan=3)

def get_text():
    global textfield
    global label
    txt = textfield.get()
    label.config(text=txt)

label = tk.Label(
    master = frame_start,
    text="This is a label",
    #foreground="white",  # Set the text color to white
    #background="black",  # Set the background color to black
)
btn = tk.Button(
    master = frame_start,
    text="click",
    bg="pink",
    fg="blue",
    command = get_text
)
textfield = tk.Entry(width=50)

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
        frame.grid(row=i, column=j)
        btn = tk.Button(master=frame, text=f"{i}{j}", width=5,height=2)
        btn.pack()


window.mainloop()
