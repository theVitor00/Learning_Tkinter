import tkinter as tk
from tkinter import ttk
from random import choice

# Main window
window = tk.Tk()
window.geometry("600x400")
window.title("Treeview")

# Data
first_names = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Taylor", "Walker", "Clark"]

# Treeview
table = ttk.Treeview(window, columns = ("First", "Last", "E-mail"), show = "headings")
table.heading("First", text = "First Name")
table.heading("Last", text = "Surname")
table.heading("E-mail", text = "E-mail")
table.pack(fill = "both", expand = True )

# Insert values into a table
#table.insert(parent = "", index = 0, values = ("John", "Doe", "johnDoe@email.com")) 
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}{last}@email.com"
    data = (first, last, email)
    table.insert(parent = "", index = 0, values = data)
    
table.insert(parent = "", index = tk.END, values = ("XXXXX", "YYYYY", "ZZZZZ"))

# Events
def item_select(event):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])
    # table.item(table.selection())

def delete_items(event):
    print("Delete")
    for i in table.selection():
        table.delete(i)

table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", delete_items)


# Run
window.mainloop()