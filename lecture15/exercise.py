"""
EXERCISE

Start the window in the middle of the screen
"""

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Exercise - Window settings")
"""
MY ANSWER
window.geometry("500x600+710+240")
"""

# instructor answer
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f"{window_width}x{window_height}+{left}+{top}")
# run
window.mainloop()