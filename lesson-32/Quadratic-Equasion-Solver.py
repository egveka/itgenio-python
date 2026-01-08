from tkinter import *
import math
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Quadratic Equation Solver")
window.resizable(False, False)

def equate():
    output.delete("1.0", END)
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        d = b**2 - 4*a*c
        answer = messagebox.askyesno("Title", f"Are you sure you want to solve the equation with {a}, {b} and {c}?")
        if not answer:
            entry_a.delete(0, END)
            entry_b.delete(0, END)
            entry_c.delete(0, END)
            return
        if d < 0:
            output.insert(END, f"Discriminant is {d}\nthe equation has no solution")
            return
        ds = math.sqrt(d)
        x1 = (-b + ds)/(2*a)
        x2 = (-b - ds)/(2*a)
        output.insert(END, f"Discriminant is {d}\nx1 = {x1}\nx2 = {x2}")
    except ValueError:
        output.insert(END, "Make sure you've entered 3 numbers!")
    except ZeroDivisionError:
        output.insert(END, "You've accidentaly divided by zero!😂")

frame = LabelFrame(text="Enter initial data")
entry_a = Entry(frame, width=5)
label = Label(frame, text="x² +")
entry_b = Entry(frame, width=5)
label2 = Label(frame, text="x+")
entry_c = Entry(frame, width=5)
label3 = Label(frame, text="= 0")
frame2 = LabelFrame(text="Solution")
output = Text(frame2, width=30, height=10)
button = Button(text="Solve Equation", command=equate)

frame.pack()
entry_a.pack(side="left")
label.pack(side="left")
entry_b.pack(side="left")
label2.pack(side="left")
entry_c.pack(side="left")
label3.pack(side="left")
frame2.pack()
output.pack()
button.pack()

window.mainloop()