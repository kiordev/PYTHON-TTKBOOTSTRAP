# Python MainRun
# Creator: Alexandr Kior (kiordev)
# Date: 15.03.2023

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

counter = 0
def count():
    global counter
    counter += 1
    my_label.config(text=counter)
    if counter >= 10:
        doh_label.pack()

# Main Setting
root = ttk.Window(themename='vapor')
root.geometry('300x300')

# Create Label
my_label = ttk.Label(root, text=counter, bootstyle='vapor')
my_label.pack(pady=30)

doh_label = ttk.Label(root, text="Dohuya", bootstyle='vapor')

# Create Button
my_button = ttk.Button(root, text='plus', bootstyle='vapor', command=count)
my_button.pack(pady=20)
root.mainloop()