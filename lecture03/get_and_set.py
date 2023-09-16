import tkinter as tk
from tkinter import ttk

def button_func():
    # get content of the entry
    entry_text = entry.get()
    
    # update the label
    # label.configure(text = "Some other text")
    label["text"] = entry_text
    entry["state"] = "disabled"
    #print(label.configure())
    
# exercise function
def reset_btn():
    label["text"] = "some text" 
    entry["state"] = "enabled"   
    
# window
window = tk.Tk()
window.title("Getting and Setting Widgets")

#widgets
label = ttk.Label(master = window, text = "Text")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = "The Button", command = button_func)
button.pack()

# exercise button
btn_reset = ttk.Button(master = window, text = "reset", command = reset_btn)
btn_reset.pack()


# exercise
# add another button that changes text back to 'some text and that enables entry

# run
window.mainloop()