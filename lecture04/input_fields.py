from tkinter import *

# root widget
root = Tk()

# entry fields, with some config parameters
e = Entry(root, width=50)
e.pack()
# get the values of the input to be used in whatever operations
# e.get()

# defines a default value to the input field, like a placeholder
e.insert(0, "Enter your first name...")


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()
    
# creating a BUTTON widget
my_button = Button(root, text = "Enter your name", padx=50, command = my_click, bg="blue", fg="white")

# put it on screen
my_button.pack()

root.mainloop()