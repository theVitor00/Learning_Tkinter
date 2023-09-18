import tkinter as tk
from tkinter import ttk

# funtions
def get_pos(event):
    print(f"x: {event.x} | y: {event.y}")

# main window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "A button")
btn.pack()

# events
btn.bind("<Alt-KeyPress-a>", lambda event: print("An event"))
text.bind("<Motion>", get_pos)
window.bind("<KeyPress>", lambda event: print(f"Button [{event.char}] was pressed."))
entry.bind("<FocusIn>", lambda event: print("Entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("Entry field was deselected"))

# run
window.mainloop()

"""
MODEL:
    widget.bind("<Event Modifier - Keypress - [key]>")
    
EVENT MODIFIERS:
    - Alt = Alt key is held;
    - Control = Ctrl key is held;
    - Shift = Shif key is held;
    - Any = <Any-KeyPress> applies to the keypress of any key

more info on: https://www.pythontutorial.net/tkinter/tkinter-event-binding/

"""