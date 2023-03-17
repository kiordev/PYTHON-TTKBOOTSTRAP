import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

window = tkb.Window(themename='vapor')
window.geometry('600x600')
window.resizable(False, False)

def clicker():
    language_label.config(text=f"{my_combo.get()}")

def click_bind(e):
    language_label.config(text=f"{my_combo.get()}")

language_label = tkb.Label(window, text='English', font=('Gotham', 25))
language_label.pack(pady=30)

# Combo Box
language = ['English', 'Українська', 'Русский']

# Combo Box
my_combo = tkb.Combobox(window, bootstyle='danger', values=language)
my_combo.pack(pady=20)

# Set Combo Default
my_combo.current(0)

# Create a button
my_button = tkb.Button(window, text='Accept', command=clicker, bootstyle='danger')
my_button.pack()

# Bind combo box
my_combo.bind("<<ComboboxSelected>>", click_bind)

window.mainloop()