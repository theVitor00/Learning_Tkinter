from tkinter import *

# root widget
root = Tk()

def my_click():
    my_label = Label(root, text="Look, i clicked a Button!!")
    my_label.pack()
    
# creating a BUTTON widget

'''
BUTTON SETTINS:

- Command = recieve a reference to executing a function when the button is clicked
- State: activated / disabled
- Padx: set width of the button in pixels
- Pady: set height of the button in pixels
- fg: set color of foreground color
- bg: set color of background color

'''
my_button = Button(root, text = "Click me!", padx=50, command = my_click, bg="blue", fg="white")

# put it on screen
my_button.pack()

root.mainloop()