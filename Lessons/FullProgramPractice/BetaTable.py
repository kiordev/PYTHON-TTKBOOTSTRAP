import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Создаем главное окно приложения
root = tk.Tk()
root.title("Записная книжка")
root.geometry("700x500")

# Создаем стиль для оформления
style = Style(theme="vapor")

# Создаем таблицу
table = ttk.Treeview(root, columns=("first", "second", "third", "fourth"), show="headings")
table.heading("first", text="Первая")
table.heading("second", text="Вторая")
table.heading("third", text="Третья")
table.heading("fourth", text="Четвертая")
table.pack(pady=10, anchor='nw')

# Создаем функцию для добавления новой строки в таблицу
def add_row():
    # Получаем значения из Entry виджетов
    first_value = first_entry.get()
    second_value = second_entry.get()
    third_value = third_entry.get()
    fourth_value = fourth_entry.get()

    # Создаем новый ряд в таблице с полученными значениями
    table.insert("", tk.END, values=(first_value, second_value, third_value, fourth_value))

    # Очищаем Entry виджеты
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    third_entry.delete(0, tk.END)
    fourth_entry.delete(0, tk.END)

# Создаем Entry виджеты для каждой колонки
first_entry = ttk.Entry(root, width=15)
second_entry = ttk.Entry(root, width=15)
third_entry = ttk.Entry(root, width=15)
fourth_entry = ttk.Entry(root, width=15)

# Создаем кнопку для добавления новой строки в таблицу
add_button = ttk.Button(root, text="Добавить новую запись", command=add_row)

# Размещаем Entry виджеты и кнопку на форме
first_entry.pack(anchor='nw', side='left', padx=10)
second_entry.pack(anchor='nw', side='left', padx=10)
third_entry.pack(anchor='nw', side='left', padx=10)
fourth_entry.pack(anchor='nw', side='left', padx=10)
add_button.pack(anchor='nw', side='left', padx=10)

# Запускаем главный цикл программы
root.mainloop()
