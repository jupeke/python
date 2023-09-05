# Some changes made by jp. Original did not respect the image aspect ratio and
# an old attribute ANTIALIAS caused a crash.

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Function to resize and save images
def resize_images():
    target_folder = target_folder_entry.get()
    max_len = int(max_size_entry.get())
    MAX_SIZE = (max_len, max_len) # added by jp
    selected_files = file_listbox.get(0, tk.END)

    if not target_folder or not max_len or not selected_files:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        for file_path in selected_files:
            image = Image.open(file_path)
            #new_width = min(max_size, image.width)
            #new_height = min(max_size, image.height)

            image.thumbnail(MAX_SIZE)   # This by jp. Otherwise did not preserve the aspect ratio.

            base_name = os.path.basename(file_path)
            modified_name = os.path.splitext(base_name)[0] + "_modified" + os.path.splitext(base_name)[1]
            save_path = os.path.join(target_folder, modified_name)
            image.save(save_path)
        messagebox.showinfo("Success", "Images resized and saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Photo Editor")

# Create and place widgets
file_label = tk.Label(root, text="Select Image Files:")
file_label.pack()

file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
file_listbox.pack()

# The point before filedialog: makes it show the filenames vertically. Hmm. No other difference noticed.
add_button = tk.Button(root, text="Add Files", \
    command=lambda: file_listbox.insert(tk.END, *filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")])))

add_button.pack()

target_folder_label = tk.Label(root, text="Target Folder:")
target_folder_label.pack()

target_folder_entry = tk.Entry(root)
target_folder_entry.pack()

# added by jp:
add_button = tk.Button(root, text="Select Target Folder", \
    command=lambda: target_folder_entry.insert(tk.END, filedialog.askdirectory())) # No point before the filedialog here!
add_button.pack()

max_size_label = tk.Label(root, text="Max Size (pixels):")
max_size_label.pack()

max_size_entry = tk.Entry(root)
max_size_entry.pack()

resize_button = tk.Button(root, text="Resize", command=resize_images)
resize_button.pack()

root.mainloop()
