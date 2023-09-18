import tkinter as tk
from tkinter import ttk

# functions
def button_func(entry_string):
    print("A button was pressed")
    print(entry_string.get())
    
def outer_func(parameter):
    def inner_func():
        print("A button was pressed")
        print(parameter.get())
    return inner_func
        
# main window
window = tk.Tk()
window.title("Functions and Arguments")
window.geometry("280x400")

# widgets
entry_string = tk.StringVar(value = "test")
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = "button", command = outer_func(entry_string))
button.pack()

# run
window.mainloop()

"""
To use a function with parameters as a command, just use 'lambda' or a inner function
to return a value to a outer function, as shown in lines 5 to 13

"""