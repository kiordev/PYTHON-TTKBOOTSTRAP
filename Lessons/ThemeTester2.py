import ttkbootstrap as tkb
from ttkbootstrap.constants import *
import tkinter as tk

# Root_Settings
root = tkb.Window(themename="vapor")
root.geometry("1000x500+450+200")
root.resizable(False, False)
root.title("Theme Tester")

def accept_theme():
    root.style.theme_use(themename=theme_list[theme_combo_box.current()])

# Root_Window_Settings
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=10)
root.columnconfigure(0, weight=1)

# Header_Root_Frame
header_root_frame = tkb.Frame(root, bootstyle='dark')
header_root_frame.grid(row=0, column=0, sticky="nsew")

# Header Combo Box Theme Accept
theme_list = root.style.theme_names()
theme_combo_box = tkb.Combobox(header_root_frame, values=theme_list)
theme_combo_box.pack(pady=10)
theme_combo_box.current()
# Header Button Theme
header_theme_button = tkb.Button(header_root_frame, text="ACCEPT", command=accept_theme)
header_theme_button.pack(pady=10)
header_theme_name = tkb.Label(header_root_frame, text="dark").pack()




# Main_Root_Frame_Settings
main_root_frame = tkb.Frame(root, bootstyle='danger')
main_root_frame.grid(row=1, column=0, sticky="nsew")
main_root_frame.columnconfigure(0, weight=1)
main_root_frame.columnconfigure(1, weight=1)
main_root_frame.rowconfigure(0, weight=1)

# Left Side Main Frame
left_side_frame = tkb.Frame(main_root_frame, bootstyle='secondary')
left_side_frame.grid(row=0, column=0, sticky="nsew")

# Left_Side_Frame_Content
tkb.Button(left_side_frame, text="outline_button", bootstyle="outline").pack(pady=10)
tkb.Label(left_side_frame, text="inverse_label", bootstyle="inverse").pack(pady=10)
tkb.Combobox(left_side_frame).pack(pady=10)
left_header_theme_name = tkb.Label(left_side_frame, text="secondary").pack(pady=10)


# Right Side Main Frame
right_side_frame = tkb.Frame(main_root_frame, bootstyle='primary')
right_side_frame.grid(row=0, column=1, sticky="nsew")

# Right_Side_Frame_Content
tkb.Button(right_side_frame, text="default_button").pack(pady=10)
tkb.Label(right_side_frame, text="default").pack(pady=10)
tkb.Combobox(right_side_frame).pack(pady=10)
right_header_theme_name = tkb.Label(right_side_frame, text="primary").pack(pady=10)


# Execute
root.mainloop()

