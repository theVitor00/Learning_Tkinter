"""
CREATE A CHECKBUTTON AND 2 RADIOBUTTONS

Radio Button:
    Values for the buttons are A and B
    Ticking either prints the value of the checkbutton
    Ticking the radio button unchecks the checkbutton
Check button:
    Ticking the checkbutton prints the value of the radio button value
    Use tkinter var for Booleans

"""

import tkinter as tk
from tkinter import ttk

# functions
def on_check_radio():
    print(check_var.get())
    check_var.set(False)


# main window
window = tk.Tk()
window.title("Exercise - Buttons")
window.geometry("400x600")

# widgets
check_var = tk.BooleanVar()
radio_var = tk.StringVar()

check = ttk.Checkbutton(
    window,
    text = "Check",
    variable = check_var,
    command = lambda: print(radio_var.get())
    )
check.pack()

radio1 = ttk.Radiobutton(
    window,
    value = "A",
    text = "Button radio 1",
    variable = radio_var,
    command = on_check_radio
    )
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    value = "B",
    text = "Button radio 2",
    variable = radio_var,
    command = on_check_radio
    )
radio2.pack()

# run
window.mainloop()