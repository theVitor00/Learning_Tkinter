# Create 2 entry fields and 1 labels. They should all be connected via StringVar()
# set a start value of "test"

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Exercise")

# tkinter variables
str_var = tk.StringVar(value = "Test")

# widgets
entry = ttk.Entry(master = window, textvariable = str_var)
entry.pack()

entry2 =ttk.Entry(master = window, textvariable = str_var)
entry2.pack()

label = ttk.Label(master = window, text = "some text", textvariable = str_var)
label.pack()

# run
window.mainloop()