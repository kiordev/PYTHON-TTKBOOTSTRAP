import ttkbootstrap as tkb
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
# Settings
main_window = tkb.Window(themename="vapor")
main_window.geometry("1000x500")
main_window.resizable(False, False)

test_label = tkb.Label(main_window, text="Сборник тестов: ", font=('Gotham', 23), bootstyle='danger')
test_label.pack(padx=60, pady=10, anchor='nw')

# Test Frame
tests_frame = ScrolledFrame(main_window, bootstyle='darkly', height=150, width=200)
tests_frame.pack(anchor='nw', pady=10, padx=10)

list = ["Some1", "Some2", "Some3", 'Some4', 'Some5', 'Some6', 'Some7', 'Some8', 'Some9']

# Button Spawn
r, c = 0, 0
for i in range(0, len(list)):
    c += 1
    tkb.Button(tests_frame, text=list[i], bootstyle='danger-outline').grid(row=r, column=c, padx=10, pady=10)
    if c >= 2:
        r, c = r+1, 0


# Execute
main_window.mainloop()
