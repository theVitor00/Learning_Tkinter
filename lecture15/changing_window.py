import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("More on the window")
window.geometry("600x400+0+0")
# window.iconbitmap("icone.ico")

# Window sizes
window.minsize(200, 100)
#window.maxsize(700, 800)
#window.resizable(True, True)

# Screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window attributes
window.attributes("-alpha", 1)
window.attributes("-topmost", True)

# Security Event
window.bind("<Escape>", lambda event: window.quit())

#window.attributes("-disable", True)
#window.attributes("-fullscreen", True)

# Title Bar
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = "se")

# Run
window.mainloop()