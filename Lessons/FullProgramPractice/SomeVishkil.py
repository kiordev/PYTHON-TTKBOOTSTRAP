import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

# Settings
window = tkb.Window(themename="vapor")
window.geometry("800x800")
window.resizable()

# First------
list_name = ["Buba Huba", "Anna Poken", "Andrew Hocharenko", "Angelina Ginger", "Alexandr Kior"]

name_label = tkb.Label(text="Alexandr Kior", font=("Gotham-bold", 25), bootstyle='danger')
name_label.pack(pady=10)

switch_name = tkb.Button(text="Switch name", bootstyle='danger-outline')
switch_name.pack(pady=10)

# Second-----
list = ["English", "Japan", "French", "German"]

language_label = tkb.Label(text="English", bootstyle='danger')
language_label.pack(pady=20)

my_combo = tkb.Combobox(values=list, bootstyle="danger")
my_combo.current(0)
my_combo.pack(pady=10)

change_button = tkb.Button(text="Change the Language", bootstyle='danger')
change_button.pack(pady=10)

cheker_label = tkb.Label(text="NONE", font=("Gotham-bold", 25), bootstyle='danger')
cheker_button = tkb.Button(text="CHECK")

cheker_label.pack(side=tkb.LEFT, padx=20)
cheker_button.pack(side=tkb.LEFT, padx=20)


# Execute
window.mainloop()