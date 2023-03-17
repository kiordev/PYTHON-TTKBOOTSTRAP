import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

window = tkb.Window(themename='vapor')
window.geometry('600x600')
window.resizable(False, False)

def set_color():
    window.style.theme_use(color_combo.get())

show_theme_color = tkb.Label(window, text='DefaultTheme', bootstyle='danger', font=('Gotham-bold', 25))
show_theme_color.pack(pady=20)
color_combo = tkb.Combobox(window, bootstyle='danger', values=window.style.theme_names())
color_combo.pack(pady=30)
btn = tkb.Button(window, bootstyle='danger', text='Accept color', command=set_color)
btn.pack(pady=20)


window.mainloop()
