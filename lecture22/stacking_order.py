import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Stacking order")
window.geometry("400x400")

# Widgets
label1 = ttk.Label(window, text = "Label 1", background = "green")
label2 = ttk.Label(window, text = "Label2", background = "red")

# label1.lift() // label1.tkraise()
# label2.lower()

button1 = ttk.Button(window, text= "Raise Label 1", command = lambda: label1.lift())
button2 = ttk.Button(window, text = "Raise button 0", command = lambda: label2.lift())

# Layout
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)

button1.place(rely = 1, relx = 0.8, anchor = "se")
button2.place(rely = 1, relx = 1, anchor = "se")

# Run
window.mainloop()