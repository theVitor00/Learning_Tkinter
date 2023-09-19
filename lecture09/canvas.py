import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# Canvas
canvas = tk.Canvas(window, bg = "white")
canvas.pack()

# .create_rectangle(left, top. right, bottom), fill, border, dash(width, gap), outline
#canvas.create_rectangle((50, 20, 200, 200), fill = "red", width = 2, dash =(2, 1), outline = "blue")

# .create_line(start_x, start_y, end_x, end_y), fill
#canvas.create_line((0, 0, 100, 150), fill = "blue")

# .create_oval(left, top, fight, bottom)
#canvas.create_oval((200, 200, 100, 100), fill = "purple")
#canvas.create_arc((200, 200, 100, 100), fill = "yellow", start = 45, extent = 180 )

# .create_polygon(x1, y1, x2, y2, x3)
#canvas.create_polygon((0, 0, 100, 200, 300, 50, 150, -50), fill = "gray")

#canvas.create_text((10, 10), text = "This is some text", fill = "blue", width = 5)

canvas.create_window((150, 100), window = ttk.Label(window, text = "This is text in a canvas"))

# run
window.mainloop()