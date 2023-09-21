import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext
from ttkbootstrap.constants import *

window = tk.Tk()
window.title("Sliders and Progress Bars")
window.geometry("500x600")

scale_int = tk.IntVar(value = 15)

scale = ttk.Scale(
    window,
    command = lambda value : progress.stop(),
    from_ = 0,
    to = 25,
    length = 300,
    orient = "vertical",
    variable = scale_int
    )
scale.pack()

progress = ttk.Progressbar(
    window,
    variable = scale_int,
    maximum = 25,
    orient = "horizontal",
    mode = "determinate",
    length = 400
    )
progress.pack()

# progress.start(1000)

scroll_text =scrolledtext.ScrolledText(window)
scroll_text.pack()

window.mainloop()