# Python TestFunc
# Creator: Alexandr Kior (kiordev)
# Date: 15.03.2023

import tkinter as tk
import ttkbootstrap as tkb
from ttkbootstrap.constants import *

def click_button():
    value = clicks.get()
    clicks.set(value + 1)
    print(clicks.get())

# Main Settings
window = tkb.Window(themename='vapor')
window.geometry('400x300')
window.resizable(False, False)

clicks = tkb.IntVar()
button = tkb.Button(window, textvariable=clicks, command=click_button)
button.pack()

window.mainloop()