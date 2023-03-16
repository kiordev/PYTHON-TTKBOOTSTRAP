# Python MainRun
# Creator: Alexandr Kior (kiordev)
# Date: 15.03.2023

import tkinter as tk
import ttkbootstrap as tkb
from ttkbootstrap.constants import *

# Main Settings
window = tkb.Window(themename='vapor')
window.geometry('400x300')
window.resizable(False, False)

# --- OPEN Functions ---
def checker():
    if check_var.get() == True or tool_cheker.get() == True:
        hello_label.config(text='GoodBye Alex!', bootstyle='danger')
    else:
        hello_label.config(text='Hello Alex!', bootstyle='vapor')
# --- CLOSE Functions ---

# --- OPEN Labels ---
# Create Hello Label
hello_label = tkb.Label(window, text="Hello Alex!", font=('Gotham', 12))
hello_label.pack(anchor=NW, padx=10, pady=10)
# --- CLOSE Labels ---

# --- OPEN Check Buttons ---
# First Check Button
check_var = tkb.IntVar()
label_changer = tkb.Checkbutton(text='Click me!', variable=check_var,
                                onvalue=True, offvalue=False,
                                command=checker, bootstyle='danger-round-toggle')
label_changer.pack(anchor=NW, padx=10, pady=10)
# --- CLOSE Check Buttons ---

# --- OPEN Tool Buttons ---
tool_cheker = tkb.IntVar()
first_tool_button = tkb.Checkbutton(text='Tool1', variable=tool_cheker,
                                onvalue=True, offvalue=False,
                                command=checker, bootstyle='danger-square-toggle')
first_tool_button.pack()

# --- CLOSE Tool Buttons ---

# Execute
window.mainloop()