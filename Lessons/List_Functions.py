# Приложение ТК для работы со списками данных
import ttkbootstrap as tkb
import tkinter as tk
from ttkbootstrap import constants

# Window settings
window = tkb.Window(themename='vapor')
window.geometry('600x700+600+150')
window.resizable(False, False)
# DEFS
def run():
    if on_off_checker.get() == 0:
        delete_element_button.configure(state='disabled')
        clear_element_button.configure(state='disabled')
        add_element_button.configure(state='disabled')
        my_combo.configure(state='disabled')
    else:
        delete_element_button.configure(state='enabled')
        clear_element_button.configure(state='enabled')
        add_element_button.configure(state='enabled')
        my_combo.configure(state='enabled')

def check_add_element_button(): # Функция для условия включения, выключения кнопки
    if len(name_list) >= 6:
        add_element_button.configure(state='disabled')
    else:
        add_element_button.configure(state='enabled')
def delete():
    name_list.pop()
    list_label.config(text=name_list)
    check_add_element_button()

def clear_list():
    name_list.clear()
    list_label.config(text=name_list)
    check_add_element_button()

def add_element():
    name_list.append(name_list_to_add[my_combo.current()])
    list_label.config(text=name_list)
    check_add_element_button()

name_list = ['Sasha', 'Ira', 'Andrew', 'Krisitina']
name_list_to_add =['Kolya', 'Mark', 'Jora', 'Sasha', 'Ira', 'Andrew', 'Krisitina']

list_label = tkb.Label(window,
                       text=name_list,
                       font=('Gotham-bold', 14), bootstyle='danger')
list_label.pack(pady=10)

# Buttons
delete_element_button = tkb.Button(window,
                                   text="Delete last element",
                                   bootstyle='danger-outline',
                                   command=delete)
delete_element_button.pack(pady=10)

clear_element_button = tkb.Button(window,
                                  text="Clear list",
                                  bootstyle='danger-outline',
                                  command=clear_list)
clear_element_button.pack(pady=10)

my_combo = tkb.Combobox(window, bootstyle='succes',
                        values=name_list_to_add)
my_combo.current(0)
my_combo.pack(pady=10)

add_element_button = tkb.Button(window, text="Add Selected Element",
                                bootstyle='danger-outline',
                                command=add_element)
add_element_button.pack(pady=10)
on_off_checker = tkb.IntVar()
on_off = tkb.Checkbutton(text="Off/On Application",
                         variable=on_off_checker, onvalue=1, offvalue=0,
                         command=run,
                         bootstyle='danger-square-toggle')
on_off.pack(pady=10)

print(len(name_list))

# Execute def

window.mainloop()