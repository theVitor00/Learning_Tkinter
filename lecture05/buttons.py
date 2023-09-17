import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

#button
def button_func():
    print("A basic button")
    print(radio_var.get())
    
button_string = tk.StringVar(value = "A button with a string var")

button = ttk.Button(window, text = "A simple button", command = button_func, textvariable = button_string)
button.pack()

# button check
check_var = tk.IntVar()
check = ttk.Checkbutton(
    window,
    text = "checkbox 1",
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5
    )
check.pack()

check2 = ttk.Checkbutton(
    window,
    text = "Checkbox 2",
    command = lambda: check_var.set(5),
    )
check2.pack()

# radio button
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(
    window,
    text = "Radiobutton 1",
    value = "Button radio 1",
    variable = radio_var,
    command = lambda: print(radio_var.get()) 
    )
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = "Radiobutton 2",
    value = "Button radio 2",
    variable = radio_var
    )

radio2.pack()

# run
window.mainloop()