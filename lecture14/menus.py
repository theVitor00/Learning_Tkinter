import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Menus")
window.geometry("600x400")

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = "New", command = lambda: print("new file"))
file_menu.add_command(label = "Open file...", command = lambda: print("Open file"))
file_menu.add_separator()
menu.add_cascade(label = "File", menu = file_menu)

# another sub menu
help_menu = tk.Menu(menu, tearoff = False)
menu.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "Help entry", command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = "Check", onvalue = "on", offvalue = "off", variable = help_check_string)

# menu button
menu_button = ttk.Menubutton(window, text = "Menu Button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = "entry 1", command = lambda: print("Test 1"))
button_sub_menu.add_checkbutton(label = "Check 1")
menu_button.configure(menu = button_sub_menu)

window.configure(menu = menu)
# run
window.mainloop()