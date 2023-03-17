from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_win = ttk.Window()
my_win.geometry('950x500')

my_theme = my_win.style.theme_names() # Обращение List темам, присвоение
print(my_theme)
print(my_win.style.colors)
my_str = ttk.StringVar(value=my_win.style.theme_use())

r, c = 0, 0
def my_update():
    my_win.style.theme_use(my_str.get())
    pass

for values in my_theme:
    rbtn = ttk.Radiobutton(my_win, text=values,
                           variable=my_str,
                           value=values,
                           command=lambda: my_update())
    rbtn.grid(row=r, column=c, padx=10, pady=20)
    c += 1
    if c > 8:
        r, c = r+1, 0

r, c = r+1, 0
for my_style in my_win.style.colors:
    btn = ttk.Button(my_win, text=my_style, bootstyle=my_style)
    btn.grid(row=r, column=c, padx=10, pady=20)
    btn1 = ttk.Button(my_win, text=my_style, bootstyle=(my_style, OUTLINE))
    btn1.grid(row=r+1, column=c, padx=10, pady=20)
    c+=1

    m = ttk.Meter(subtextstyle=my_style, metersize=100, amountused=35, bootstyle=my_style)
    m.grid(row=r+2, column=c, padx=10, pady=20)

    fg = ttk.Floodgauge(value=75, bootstyle=my_style)
    fg.grid(row=r+3, column=c, padx=10, pady=20)


my_win.mainloop()