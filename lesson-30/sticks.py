from tkinter import *
from random import randint

window = Tk()
window.geometry("400x300")
window.title("Sticks")
window.resizable(False, False)

sticks = 20
def player():
    global sticks
    value = entry_sticks.get()
    if value == "":
        return
    try:
        delete_sticks = int(value)
    except:
        entry_sticks.delete(0, END)
        return
    if delete_sticks in [1, 2, 3] and delete_sticks < sticks:
        sticks -= delete_sticks
        label_sticks.config(text=sticks*"|")
        status.config(text=sticks)
        button.config(state="disabled")
        if sticks == 1:
            status.config(text="You Won!", fg="green")
        else:
            label_move.config(text="It's computer's turn, please wait!")
            entry_sticks.delete(0, END)
            window.after(2000, computer)

def computer():
    global sticks
    delete_sticks_c = randint(1, 3)
    if delete_sticks_c < sticks:
        if sticks == 4:
            sticks -= 3
            label_sticks.config(text=sticks*"|")
        elif sticks == 3:
            sticks -= 2
            label_sticks.config(text=sticks*"|")
        else:
            sticks -= delete_sticks_c
            label_sticks.config(text=sticks*"|")
            status.config(text=sticks)
        if sticks == 1:
            status.config(text="Computer Won!", fg="red")
            button.config(state="disabled")
        else:
            label_move.config(text="Enter a number beetwen 1 and 3")
            button.config(state="normal")

label_move = Label(text="Enter a number beetwen 1 and 3", font=("arial", 15, "bold"))
entry_sticks = Entry(font=("arial", 15, "bold"))
label_sticks = Label(text=sticks*"|", font=("arial", 30, "bold"))
status = Label(font=("arial", 30, "bold"), text=sticks)
button = Button(font=("arial", 15, "bold"), text="take sticks", command=player)

label_move.pack(padx=5, pady=5)
entry_sticks.pack(padx=5, pady=5)
label_sticks.pack(padx=5, pady=5)
status.pack(padx=5, pady=5)
button.pack(padx=5, pady=5)

window.mainloop()