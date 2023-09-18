"""
EXERCISE

Print "Mousewheel" when the user holds down shift and uses the mousewheel
while text is selected

"""

import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Exercise - Event Binding")
window.geometry("600x500")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "Send")
btn.pack()

# Events
text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# Run
window.mainloop()