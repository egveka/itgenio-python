from tkinter import*

window = Tk()
window.geometry("400x300")
window.title("Data input-output")
window.resizable(False, False)

def show():
    outputbox.delete(0, END)
    password = inputbox.get()
    outputbox.insert(END, password)

passwordbox = LabelFrame(text="password")
label1 = Label(passwordbox, text="Enter your password:")
label2 = Label(passwordbox, text="Your password")
showbutton = Button(passwordbox, text="show", command=show)
inputbox = Entry(passwordbox, bg="black", fg="white", relief=RAISED, justify=CENTER, width=20, state=NORMAL, show="*")
outputbox = Entry(passwordbox, width=20, justify=CENTER)

passwordbox.pack(padx=5, pady=5)
label1.pack(padx=5, pady=5)
inputbox.pack(padx=5, pady=5)
label2.pack(padx=5, pady=5)
outputbox.pack(padx=5, pady=5)
showbutton.pack(padx=5, pady=5)

window.mainloop()