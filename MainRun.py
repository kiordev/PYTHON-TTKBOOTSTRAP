import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

window = tkb.Window(themename='vapor')
window.geometry('600x600')
window.resizable(False, False)

my_label = tkb.Label()

for button_r in range(1,4):
    for button_c in range(1,4):
        btn = tkb.Button(window, text=button_r, bootstyle='vapor-outline')
        btn.grid(row=button_r, column=button_c, padx=10, pady=10)

window.mainloop()