import time
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

# Settings
window = tkb.Window(themename='vapor')
window.geometry('600x700+600+150')
window.resizable(False, False)

global step
step = 0
def timer():
    global step
    step += 1
    my_meter.amountusedvar.set(value=step)


my_meter = tkb.Meter(window,
                     subtext='Timer',
                     interactive=False,
                     bootstyle='danger',
                     stripethickness=6,
                     textright='sec',
                     amounttotal=60
                     )
my_meter.pack(pady=10)

add_button = tkb.Button(text="Start Timer", bootstyle='danger-outline', command=timer)
add_button.pack(pady=10)


# Little Doc:
# subtext = "888" # Главный текст
# interactive (False, True) - Выключает тянучку за курсором
# textright / textleft - можно дописать текст до,после цифры
# metertype (full, semi) - тип метера, полный, неполный
# stripethickness (цифра) - ширина кусочка
# metersize (цифра) - диаметр метра
# amountused (цифра) - заполненная часть
# amounttotal - Общее количество
# subtextstyle - замена стиля текста

# Execute
window.mainloop()

