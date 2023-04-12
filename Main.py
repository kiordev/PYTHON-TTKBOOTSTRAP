import ttkbootstrap as tkb
import Lessons.Human as hm
# Settings
window = tkb.Window(themename='vapor')
window.resizable(False, False)
window.geometry('800x500+600+100')
window.title('Testing Application')

list = ["First", "Second", "Third", "First", "Second", "Third"]

for i in range(0, len(list)):
    tkb.Button(window, text=list[i], bootstyle='danger', width=10).pack(pady=10, padx=10, anchor='nw')

# Execute
window.mainloop()