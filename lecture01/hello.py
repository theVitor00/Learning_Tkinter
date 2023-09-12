from tkinter import *


'''
TO CREATE ANYTHING WITH TKINTER, FIRST WE HAVE TO DEFINE THE THING
AND THEN PUT IT ON THE SCREEN. 
2 STEPS FOR EVERY SINGE WIDGET
'''

# root widget
root = Tk()

# STEP 1 - creating a new label widget and linking it to root widget
myLabel = Label(root, text = "Hello World!")

# STEP 2 - Shoving it onto the screen
myLabel.pack()

# create a main loop to hold the window while true
root.mainloop()