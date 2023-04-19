import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import tkinter as tk


def speak():
    my_label.config(text=f" You typied: {my_entry.get()}")

# Root_Settings
root = tkb.Window(themename="vapor")
root.geometry("1000x500+450+200")
root.resizable(False, False)
root.title("Theme Tester")

my_entry = tkb.Entry(root, width=100)
my_entry.pack(pady=50)

my_button = tkb.Button(root,
                       bootstyle='danger-outline',
                       text='Accept',
                       command=speak)
my_button.pack(pady=10)

my_label = tkb.Label(root, text="")
my_label.pack(pady=10)

# Execute
root.mainloop()

