import ttkbootstrap as tkb

# Window settings
window = tkb.Window(themename='vapor')
window.geometry('600x700+600+150')
window.resizable(False, False)

def accept_data():
    if login_entry.get() == 'sasha' and password_entry.get() == 'kior':
        accept_button.config(bootstyle='succes-outline')
        password_entry.config(bootstyle='succes')
        login_entry.config(bootstyle='succes')
    else:
        accept_button.config(bootstyle='danger-outline')
        password_entry.config(bootstyle='danger')
        login_entry.config(bootstyle='danger')

login_label = tkb.Label(window, text="Login: ")
login_label.grid(row=1, column=1, stick='W', pady=20)

login_entry = tkb.Entry(window)
login_entry.grid(row=1, column=2, padx=25)

password_label = tkb.Label(window, text="Password: ")
password_label.grid(row=2, column=1, stick='W', pady=10)

password_entry = tkb.Entry(window)
password_entry.grid(row=2, column=2, padx=25)

accept_button = tkb.Button(window, bootstyle='succes', text='Accept', command=accept_data)
accept_button.grid(row=3, column=2, pady=25)

window.mainloop()
