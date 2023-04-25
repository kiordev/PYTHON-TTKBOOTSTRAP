import ttkbootstrap as tkb
import tkinter as tk
# Settings
window = tkb.Window(themename='vapor')
window.geometry("800x600")
window.resizable(False, False)

# Main_Window_Grid_Settings
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

side_frame = tkb.Frame(window)
side_frame.grid(row=0, column=0, sticky="nsew")

# Side Frame Content
menu_label = tkb.Label(side_frame, text="Menu", font=("Gotham-bold", 20), bootstyle='vapor')
menu_label.pack(padx=10, pady=10)

# Center Frame Content
center_frame = tkb.Frame(window, bootstyle="light")
center_frame.grid(row=0, column=1, sticky="nsew")

# Center_Frame_Grid_Settings
center_frame.rowconfigure(0, weight=1)
center_frame.rowconfigure(1, weight=15)
center_frame.columnconfigure(0, weight=1)

up_center_frame = tkb.Frame(center_frame, bootstyle='primary')
up_center_frame.grid(row=0, column=0, sticky="nsew")

down_center_frame = tkb.Frame(center_frame, bootstyle='secondary')
down_center_frame.grid(row=1, column=0, sticky="nsew")

# Execute
window.mainloop()