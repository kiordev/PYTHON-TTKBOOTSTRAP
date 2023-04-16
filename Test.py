import ttkbootstrap as tkb

root = tkb.Window()
root.geometry("300x300")


def counter():
    counter = num.get()
    num.set(counter+1)


num = tkb.IntVar(value=0)

my_button = tkb.Button(textvariable=num, command=counter)
my_button.pack()
root.mainloop()