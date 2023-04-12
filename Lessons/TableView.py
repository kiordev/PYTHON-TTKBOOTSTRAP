import ttkbootstrap as tkb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

window = tkb.Window(themename='superhero')
colors = window.style.colors # Список с цветами (такое уже делал)
window.geometry('1000x600')
window.resizable(False, False)

colums = [
    {'text':'LicenseNumber', "stretch": False},
    {'text': 'Company', "stretch": False},
    {'text': 'UserCount', "stretch": False},
]
row_data = [
    ("A123", "IzzyCo", 12),
    ("A136", "Kimdee", 45),
    ("A158", "Farmading Co", 36),
    ("A123", "IzzyCo", 12),
    ("A136", "Kimdee", 45),
    ("A158", "Farmading Co", 36)


]

table = Tableview(window,
                  coldata=colums, rowdata=row_data,
                  paginated=True,
                  autofit=False,
                  searchable=True,
                  bootstyle='danger',
                  stripecolor=(colors.light, 'red')
)

table.pack(fill=BOTH, expand=YES, padx=10, pady=10)

table.insert_row('end', ["Marzale", 26])
table.load_table_data()

rows=table.tablerows
print(rows[1].values)


window.mainloop()
