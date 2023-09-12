from tkinter import *

# root widget
root = Tk()

# STEP 1 - creating a new label widget and linking it to root widget
myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "My name is Pablo Vitor").grid(row = 1, column = 5)
myLabel3 = Label(root, text = "Monalisa").grid(row = 1, column = 1)

# STEP 2 - Shoving it onto the screen using Grid System to order elements on screen
# myLabel1.grid(row = 0, column = 0)
# myLabel2.grid(row = 1, column = 5)
# myLabel3.grid(row = 1, column = 1)

# create a main loop to hold the window while true
root.mainloop()