from tkinter import*
from tkinter import ttk

window = Tk()
window.geometry("400x300")
window.title("Data input-output")
window.resizable(False, False)

def show():
    password = inputbox.get()
    digit_counter = 0
    low_counter = 0
    high_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
        if char.islower():
            low_counter += 1
        if char.isupper():
            high_counter += 1
    if digit_counter < 1 and len(password) < 10 \
        or digit_counter < 1 and high_counter < 1 \
        or digit_counter < 1 and low_counter < 1 \
        or len(password) < 10 and high_counter < 1 \
        or len(password) < 10 and low_counter < 1 \
        or low_counter < 1 and high_counter < 1:
        label2.config(text="Several conditions are not met!", fg="red")
    elif len(password) < 10:
        label2.config(text="Password is too short!", fg="red")
    elif low_counter < 1:
        label2.config(text="Not enough lowercase letters!", fg="red")
    elif high_counter < 1:
        label2.config(text="Not enough uppercase letters!", fg="red")
    elif digit_counter < 1:
        label2.config(text="Not enough digits!", fg="red")
    else:
        label2.config(text="Password is OK!", fg="lime green")

def theme():
    window.config(bg="#353535")
    passwordbox.config(bg="#353535", fg="white")
    label1.config(bg="#353535", fg="white")
    label2.config(bg="#353535", fg="white")
    style = ttk.Style()
    style.configure("My.TButton", background="red", foreground="white")
    showbutton.config(style="MY.TButton")
    change_theme.config(style="MY.TButton",state=DISABLED)

passwordbox = LabelFrame(text="password")
label1 = Label(passwordbox, text="Enter your password:")
label2 = Label(passwordbox)
showbutton = ttk.Button(passwordbox, text="show", command=show, width=10)
inputbox = Entry(passwordbox, bg="black", fg="white", relief=RAISED, justify=CENTER, width=20, state=NORMAL, show="*")
change_theme = ttk.Button(passwordbox, text="Change theme", command=theme, width=10)
message = Label(passwordbox)

passwordbox.pack(padx=5, pady=5)
label1.pack(padx=5, pady=5)
inputbox.pack(padx=5, pady=5)
label2.pack(padx=5, pady=5)
showbutton.pack(padx=5, pady=5)
change_theme.pack(padx=5, pady=5)

window.mainloop()