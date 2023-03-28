import ttkbootstrap as tkb

window = tkb.Window(themename='vapor')

window.title("NoteBookWidget")
window.geometry('500x400')

my_notebook = tkb.Notebook(window, bootstyle='dark')
my_notebook.pack(pady=20)

tab1 = tkb.Frame(my_notebook)
tab2 = tkb.Frame(my_notebook)

my_label = tkb.Label(tab1, text="My Awesome Label!", font=('Helvetica', 18))
my_label.pack(pady=20)

my_text = tkb.Text(tab1, width=70, height=10)
my_text.pack(pady=10, padx=10)

my_text1 = tkb.Text(tab2, width=70, height=10)
my_text1.pack(pady=10, padx=10)

my_button = tkb.Button(tab1, text="Click me!", bootstyle='danger-outline')
my_button.pack(pady=2)

my_label2 = tkb.Label(tab2, text="Balalalala", font=('Helvetica', 18))
my_label2.pack(pady=20)

#Add frames

my_notebook.add(tab1, text='Tab one')
my_notebook.add(tab2, text='Tab two')


window.mainloop()