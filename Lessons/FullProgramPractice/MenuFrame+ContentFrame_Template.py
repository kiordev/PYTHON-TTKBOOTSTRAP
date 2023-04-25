import ttkbootstrap as tkb
import tkinter as t
from ttkbootstrap import constants

# Settings
window = tkb.Window()
window.geometry("800x600")
window.resizable(False, False)

# Grid_Settings
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)

# Функция для работы логина/пароля
def accept_data():
    if login_entry.get() == 'sasha' and password_entry.get() == 'kior':
        accept_button.config(bootstyle='succes-outline')
        password_entry.config(bootstyle='succes')
        login_entry.config(bootstyle='succes')
    else:
        accept_button.config(bootstyle='danger-outline')
        password_entry.config(bootstyle='danger')
        login_entry.config(bootstyle='danger')

def accept_theme():
    window.style.theme_use(themename=my_theme[theme_combobox.current()])

# Side_Frame
side_frame = tkb.Frame(window, bootstyle='dark')
side_frame.grid(row=0, column=0, sticky="nsew")

menu_label = tkb.Label(side_frame, text="Menu", font=("Gotham-bold", 20), bootstyle='inverse-dark')
menu_label.pack(padx=10, pady=10)

list_menu = ["NEW GAME", "LOAD GAME", "OPTIONS", "CREDITS", "EXIT"]
i = 0
for i in range(0, 5):
    tkb.Button(side_frame, text=list_menu[i], bootstyle="primary-outline", width=25).pack(pady=20, padx=10,)
    i += 1

# Change Theme
my_theme = window.style.theme_names()
theme_combobox = tkb.Combobox(side_frame, values=my_theme)
theme_combobox.pack(pady=20, padx=10)
accept_theme_button = tkb.Button(side_frame, bootstyle='info-outline', text='ACCEPT THEME', command=accept_theme)
accept_theme_button.pack(pady=20, padx=10)

# Main_Frame
main_frame = tkb.Frame(window, bootstyle='primary')
main_frame.grid(row=0, column=1, sticky="nsew")

login_label = tkb.Label(main_frame, text="Login: ", bootstyle='inverse-primary', font=("Gotham-bold", 10))
login_label.grid(row=1, column=1, stick='W', pady=20, padx=30)

login_entry = tkb.Entry(main_frame)
login_entry.grid(row=1, column=2, padx=25)

password_label = tkb.Label(main_frame, text="Password: ", bootstyle='inverse-primary', font=("Gotham-bold", 10))
password_label.grid(row=2, column=1, stick='W', pady=10, padx=30)

password_entry = tkb.Entry(main_frame)
password_entry.grid(row=2, column=2, padx=25)

accept_button = tkb.Button(main_frame, bootstyle='info-outline', text='Accept', command=accept_data)
accept_button.grid(row=3, column=2, pady=25)

window.mainloop()