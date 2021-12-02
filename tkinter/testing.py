import tkinter as tk
window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=20,
    height=10
)
label.pack()

btn = tk.Button(
    text="click",
    width=25,
    height=5,
    bg="pink",
    fg="blue",
)
btn.pack()
window.mainloop()
