"""
EXERCISE

Add a third label and button
"""


import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Exercise - Stacking")
window.geometry("400x400")

label1 = ttk.Label(window, text = "Label 1", background = "green")
label2 = ttk.Label(window, text = "Label 2", background = "red")
label3 = ttk.Label(window, text = "Label Exercise", background = "blue")

button1 = ttk.Button(window, text = "Raise label 1", command = lambda: label1.lift())
button2 = ttk.Button(window, text = "Raise label 2", command = lambda: label2.lift())
button3 = ttk.Button(window, text = "Raise button 3", command = lambda: label3.lift())

label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)
label3.place(x = 200, y = 20, width = 80, height = 150)

button1.place(rely = 1, relx = 0.8, anchor = "se")
button2.place(rely = 1, relx = 1, anchor = "se")
button3.place(rely = 1, relx = 0.6, anchor = "se")


window.mainloop()