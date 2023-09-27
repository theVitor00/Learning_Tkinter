# REPRODUCE THE LAYOUT SHOWN ON THE SCREEN

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Exercise")
window.geometry("400x600")

label1 = ttk.Label(window, text = "First label", back = "red")
label2 = ttk.Label(window, text = "Label 2", background = "blue")
label3 = ttk.Label(window, text = "Last of the labels", background = "green")
button = ttk.Button(window, text = "button")

label1.pack(side = "top", fill = "x")
label2.pack(side = "top", expand = True)
label3.pack(side = "top", expand = True, fill = "both")
button.pack(side = "top", fill = "x")

window.mainloop()