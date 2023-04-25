import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *

class NextWindow(tkb.Toplevel):
    def __init__(self):
        super().__init__()
        # Settings
        self.title("ФОРМА ЛОГИНА И ПАРОЛЯ")
        self.geometry('500x500')
        self.resizable(False, False)
        # Login
        self.login_label = tkb.Label(self, bootstyle='danger', text="LOGIN: ", font=("Gotham-bold", 10))
        self.login_label.pack(pady=10)

        # Password
        self.password_label = tkb.Label(self, bootstyle='danger', text="PASSWORD: ", font=("Gotham-bold", 10))
        self.password_label.pack(pady=10)





