import ttkbootstrap as tkb
import tkinter as tk
# Settings
window = tkb.Window(themename='vapor')
window.geometry("500x1980")
window.resizable(False, False)

def accept_theme():
    window.style.theme_use(themename=my_theme[theme_combobox.current()])

# ComboBoxThemeArray
my_theme = window.style.theme_names()
my_str = tkb.StringVar(value=window.style.theme_use())
theme_combobox = tkb.Combobox(window, values=my_theme)
theme_combobox.pack(pady=20, padx=10)
accept_theme_button = tkb.Button(window, bootstyle='info-outline', text='ACCEPT THEME', command=accept_theme)
accept_theme_button.pack(pady=20, padx=10)

style_list = ["primary", "secondaryy", "success", "info", "warning", "danger", "light", "dark"]
i = 0
for i, word in enumerate(style_list):
    tkb.Button(text=style_list[i], bootstyle=style_list[i], width=10).pack(pady=10)




# Execute
window.mainloop()