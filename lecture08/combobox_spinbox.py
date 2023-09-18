import tkinter as tk
from tkinter import ttk

# Main window
window = tk.Tk()
window.title("Combo and Spin")
window.geometry("600x400")

# combobox
items = ("Ice cream", "Pizza", "Brocolli", "Sandwich", "Lasagna")
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
#combo["values"] = items
combo.configure(values = items)
combo.pack()

# Label
combo_label = ttk.Label(window, text = "A Label")
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window,
    from_ =3,
    to = 20,
    increment = 3,
    command = lambda: print(spin_int.get()),
    textvariable = spin_int
    )
spin.bind("<<Increment>>", lambda event: print("Up"))
spin.bind("<<Decrement>>", lambda event: print("Down"))
#spin["value"] = (1, 2, 3,4, 5, 6)
spin.pack()

# Events
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text = f"Selected Value: {food_string.get()}"))

# run 
window.mainloop()
