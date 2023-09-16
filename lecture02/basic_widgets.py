import tkinter as tk
from tkinter import ttk

def button_func():
    print("A button was pressed")
    
def say_hello():
    print("Hello")

# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master = window, text = "This is a test")
label.pack()

#ttk text
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#Exercise: add one more text label and a button with a function that prints hello 
my_label = tk.Label(master = window, text = "my label")
my_label.pack()

#btn_hello = ttk.Button(master = window, text = "hello", command = say_hello)
btn_hello = ttk.Button(master = window, text = "hello", command = lambda: print("Hello guys"))
btn_hello.pack()

#ttk button
button = ttk.Button(master = window, text = "Send", command= button_func)
button.pack()

# run
window.mainloop()


'''

 LAMBDA

Usada para executar funções simples e que não exigam operações complexas
dentro da propria declaração do widget, como na linha 32

'''