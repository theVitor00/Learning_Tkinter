"""
EXERCISE

Create anoter frame with a label, a button and an entry and place it 
to the right of the other widgetd

"""

import tkinter as tk
from tkinter import ttk

# Main Window
window = tk.Tk()
window.geometry("600x400")
window.title("Frames and Parenting")

# Frame
frame = ttk.Frame(window, width=200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False) # set dynamic height and width to True or False
frame.pack(side = "left")

# Master setting
label = ttk.Label(frame, text = "Label in frame")
label.pack()

button = ttk.Button(frame, text = "Button in a frame")
button.pack()

# example
label2 = ttk.Label(window, text = "Label outside frame")
label2.pack()

# Exercise
frame2 = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side = "right")

label3 = ttk.Label(frame2, text = "Exercise label")
label3.pack()

button = ttk.Button(frame2, text = "Ex Button")
button.pack()

entry = ttk.Entry(frame2)
entry.pack()

# Run
window.mainloop()