import ttkbootstrap as tkb

window = tkb.Window(themename='vapor')

window.title("NoteBookWidget")
window.geometry('500x400')

def save_notes():
    notes = my_text.get('1.0', 'end-1c')
    file = open('notes.txt', 'w')
    file.write(notes)
    print("NOTE SAVED!")


my_notebook = tkb.Notebook(window, bootstyle='dark')
my_notebook.pack(pady=20)
tab1 = tkb.Frame(my_notebook)
my_text = tkb.Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

main_menu = tkb.Menu(window)
window.config(menu=main_menu)

file_menu = tkb.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="Save", command=save_notes)

try:
    with open('notes.txt', 'r') as f:
        notes = f.read()
        my_text.insert('end', notes)
except FileNotFoundError:
    pass

#Add frames
my_notebook.add(tab1, text='Tab one')

save_button = tkb.Button(window, text="Save", command=save_notes)
save_button.pack(side="right")

window.mainloop()