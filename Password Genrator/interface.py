from tkinter import *

window = Tk()
window.geometry("300x200")
window.title("Password Generator")
window.resizable(False, False)

lf_symbols = LabelFrame(text="SYMBOL")

lowercase = BooleanVar()
number = BooleanVar()
uppercase = BooleanVar()
special = BooleanVar()

check_lowercase = Checkbutton(lf_symbols, text="abcdefghijklmnopqrstuvwxyz", variable=lowercase, offvalue=False, onvalue=True)
check_numbers = Checkbutton(lf_symbols, text="0123456789", variable=number, offvalue=False, onvalue=True)
check_uppercase = Checkbutton(lf_symbols, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", variable=uppercase, offvalue=False, onvalue=True)
check_special = Checkbutton(lf_symbols, text="!@#$%^&*():;|\/><,.~`±§-_", variable=special, offvalue=False, onvalue=True)
password_e = Entry(lf_symbols)
button = Button(lf_symbols, text="GENERATE A PASSWORD")

lf_symbols.pack()
check_lowercase.pack(anchor=W)
check_numbers.pack(anchor=W)
check_uppercase.pack(anchor=W)
check_special.pack(anchor=W)
password_e.pack()
button.pack()