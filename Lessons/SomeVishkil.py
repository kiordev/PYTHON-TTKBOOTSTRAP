import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

# Settings
window = tkb.Window(themename="vapor")
window.geometry("800x800")
window.resizable()

counter = 0
def switch_name():
    global counter
    if counter > 4:
        counter = 0
        name_label.config(text=list_name[counter])
    else:
        name_label.config(text=list_name[counter])
    counter += 1
    pass

def change_word():
    language_label.config(text=f'{my_combo.get()}')

def check_num():
    left = left_meter.amountusedvar.get()
    right = right_meter.amountusedvar.get()

    if left > right:
        cheker_label.config(text="LEFT", bootstyle='success')
    else:
        cheker_label.config(text="RIGHT", bootstyle='danger')

# First------
list_name = ["Buba Huba", "Anna Poken", "Andrew Hocharenko", "Angelina Ginger", "Alexandr Kior"]

name_label = tkb.Label(text="Alexandr Kior", font=("Gotham-bold", 25), bootstyle='danger')
name_label.pack(pady=10)

switch_name = tkb.Button(text="Switch name", bootstyle='danger-outline', command=switch_name)
switch_name.pack(pady=10)

# Second-----
list = ["English", "Japan", "French", "German"]

language_label = tkb.Label(text="English", bootstyle='danger')
language_label.pack(pady=20)

my_combo = tkb.Combobox(values=list, bootstyle="danger")
my_combo.current(0)
my_combo.pack(pady=10)

change_button = tkb.Button(text="Change the Language", bootstyle='danger', command=change_word)
change_button.pack(pady=10)

# Third---

left_meter = tkb.Meter(
    subtext="LEFT",
    interactive=True,
    bootstyle='success',
    stripethickness=6,
    textright='sec',
    amounttotal=100
)
right_meter = tkb.Meter(
    subtext="RIGHT",
    interactive=True,
    bootstyle='danger',
    stripethickness=6,
    textright='sec',
    amounttotal=100
)

cheker_label = tkb.Label(text="NONE", font=("Gotham-bold", 25), bootstyle='danger')

cheker_button = tkb.Button(text="CHECK", command=check_num)

right_meter.pack(side=tkb.LEFT, padx=20)
cheker_label.pack(side=tkb.LEFT, padx=20)
cheker_button.pack(side=tkb.LEFT, padx=20)
left_meter.pack(side=tkb.LEFT, padx=20)

# Execute
window.mainloop()