import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap.constants import *
from root import NextWindow

class PasswordLoginForm(tkb.Window):
    def __init__(self):
        super().__init__()
        # Settings
        self.title("ФОРМА ЛОГИНА И ПАРОЛЯ")
        self.geometry('500x500')
        self.resizable(False, False)
        self.style.theme_use("superhero")

        # L and P
        self.password = "1"
        self.login = "1"

        # Login
        self.login_label = tkb.Label(bootstyle='danger', text="LOGIN: ", font=("Gotham-bold", 10))
        self.login_label.pack(pady=10)
        self.login_entry = tkb.Entry(width=15, show="*")
        self.login_entry.pack(pady=10)

        # Password
        self.password_label = tkb.Label(bootstyle='danger', text="PASSWORD: ", font=("Gotham-bold", 10))
        self.password_label.pack(pady=10)
        self.password_label = tkb.Entry(width=15, show="*")
        self.password_label.pack(pady=10)

        # CheckButton
        self.button = tkb.Button(bootstyle='danger', text="CHECK", width=10, command=self.validation)
        self.button.pack(pady=10)

    def validation(self):
        if self.password == "1" and self.login == "1":
            window = NextWindow()
            window.mainloop()

if __name__ == "__main__":
    app = PasswordLoginForm()
    app.mainloop()


