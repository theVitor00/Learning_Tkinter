import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.geometry("600x400")
window.title("Hide widgets")

# place

'''def hide_label_place():
    label.place_forget()
    
def show_label_place():
    label.place(relx = 0.5, rely = 0.5, anchor = "center")
    

button = ttk.Button(window, text = "Hide label", command = hide_label_place)
button.place(x = 10, y = 10)

button2 = ttk.Button(window, text = "Show label", command = show_label_place)
button2.place(x = 90, y = 10)

label = ttk.Label(window, text = "A Label")
label.place(relx = 0.5, rely = 0.5, anchor = "center")'''


# Grid


"""def toggle_label_grid():
    global label_visible
    
    if label_visible:
        label.grid_forget()
        label_visible = False
    else:
        label_visible = True
        label.grid(column = 1, row = 0)


window.columnconfigure((0,1), weight = 1, uniform = "a")
window.rowconfigure(0, weight = 1, uniform = "a")

button = ttk.Button(window, text = "Toggle Label", command = toggle_label_grid)
button.grid(column = 0, row = 0)

label_visible = True
label = ttk.Label(window, text = "A Label")
label.grid(column = 1, row = 0)"""


# Pack
def toggle_label_pack():
    global label_visible
    
    if label_visible:
        label["text"] = ""
        label_visible = False
    else:
        label_visible = True
        label["text"] = "A Label"

label_visible = True
label = ttk.Label(window, text = "A Label")
label.pack(expand = True)

button = ttk.Button(window, text = "Toggle Label", command = toggle_label_pack)
button.pack()

# Run
window.mainloop()