"""
EXERCISE

Create a Spinbox that contains the letters A B C D E
and print the value whenever the value is decreased

"""

import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Exercise: Spinbox")
window.geometry("400x600")

# Widgets
spin_var = tk.StringVar(value = " ... ")
spin = ttk.Spinbox(window, textvariable = spin_var)
spin["value"] = ("A", "B", "C", "D", "E")
spin.pack()

# Event bindings
spin.bind("<<Decrement>>", lambda event: print(spin_var.get()))

# Run
window.mainloop()