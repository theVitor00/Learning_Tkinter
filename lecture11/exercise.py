"""
EXERCISE

Create a progress that is vertical, starts automatically and also show the progress as a number
there should also be a scale slider that is affected by the progress bar


"""
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("EXERCISE: Sliders and Progress Bars")
window.geometry("500x600")


str_slider = tk.StringVar()

label = tk.Label(window, text = "", textvariable = str_slider)
label.pack()

progress = ttk.Progressbar(
    window,
    orient = "vertical",
    variable = str_slider,
    length = 150,
    maximum = 100,
    )
progress.pack()
progress.start()

slider = ttk.Scale(window, length = 150, orient = "horizontal", from_ = 0, to = 100, variable = str_slider)
slider.pack()

window.mainloop()