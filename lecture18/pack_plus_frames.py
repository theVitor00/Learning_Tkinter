import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Pack Parenting")
window.geometry("400x600")

# Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = "First Label", background = "red")
label2 = ttk.Label(top_frame, text =  "Label 2", background = "blue")

# Middle Widget
label3 = ttk.Label(window,text = "Another Label", background = "green")

# Bottom Frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = "Last of labels", background = "orange")
button = ttk.Button(bottom_frame, text = "A Button")
button2 = ttk.Button(bottom_frame, text = "Another Button")

# Top Layout
label1.pack(side = "left", fill = "both", expand = True)
label2.pack(side = "left", fill = "both", expand = True)
top_frame.pack(fill = "both", expand = True)

# Middle Layout
label3.pack(expand = True)

# Bottom Layout
button.pack(side = "left", expand = True, fill = "both")
label4.pack(side = "left", expand = True, fill = "both")
button2.pack(side = "left", expand = True, fill = "both")
bottom_frame.pack(expand = True, fill = "both", padx = 20, pady = 20)

# Run
window.mainloop()