import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class App(tkb.Window): # Создаем класс App, которое полностью наследует класс tkb.Window
    def __init__(self, title, size): # Создаем конструктор класса
        super().__init__() # Метод super нужен, чтобы получить доступ ко всему что есть в tkb.Window
        self.geometry(size)
        self.title(title)
        self.style.theme_use(themename='vapor')

        self.mainloop()

class Menu(tkb.Frame):
    def __init__(self, master):
        super().__init__()

App("Same chit aspp", ("500x500")) # Передаем параметры для конструктора в классе