import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("Button pressed")

# window
window = tk.Tk()
window.title("Tkinter Variables")

# tkinter variables
string_var = tk.StringVar(value = "star value") 

# widgets
label = ttk.Label(master = window, text = "Label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

# run
window.mainloop()