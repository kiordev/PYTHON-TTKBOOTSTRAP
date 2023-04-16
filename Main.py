import ttkbootstrap as tkb
import tkinter as t
from ttkbootstrap import constants

# Settings
window = tkb.Window(themename='vapor')
window.geometry("800x600")
window.resizable(False, False)

# Grid_Settings
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)

# Функция для работы логина/пароля
def counter():
    counter = num.get()
    num.set(counter+1)

# Side_Frame
side_frame = tkb.Frame(window, bootstyle='dark')
side_frame.grid(row=0, column=0, sticky="nsew")

menu_label = tkb.Label(side_frame, text="Menu", font=("Gotham-bold", 20), bootstyle='inverse-dark')
menu_label.pack(padx=10, pady=10)

list_menu = ["NEW GAME", "LOAD GAME", "OPTIONS", "CREDITS", "EXIT"]

new_game_button = tkb.Button(side_frame, text="NEW GAME", bootstyle="primary-outline", command=lambda: main_frame.tkraise(), width=25)
new_game_button.pack(pady=20, padx=10)
load_game_button = tkb.Button(side_frame, text="LOAD GAME", bootstyle="primary-outline", command=lambda: Load_frame.tkraise(), width=25)
load_game_button.pack(pady=20, padx=10)

num = tkb.IntVar()

# NewGame_Frame
main_frame = tkb.Frame(window, bootstyle='primary')
main_frame.grid(row=0, column=1, sticky="nsew")
newgame_label = tkb.Label(main_frame, text="New game", font=("Gotham-bold", 20), bootstyle='inverse-dark')
newgame_label.pack(padx=10, pady=10)
test_game_button = tkb.Button(main_frame, textvariable=num, bootstyle='dark', command=counter)
test_game_button.pack()

# LoadGame_Frame
Load_frame = tkb.Frame(window, bootstyle='primary')
Load_frame.grid(row=0, column=1, sticky="nsew")
load_label = tkb.Label(Load_frame, text="Load Game", font=("Gotham-bold", 20), bootstyle='inverse-dark')
load_label.pack(padx=10, pady=10)

load_game_button = tkb.Button(Load_frame, textvariable=num, bootstyle='danger', command=counter)
load_game_button.pack()

main_frame.tkraise()

window.mainloop()