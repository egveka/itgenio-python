from tkinter import *
import math
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Quadratic Equation Solver")
window.resizable(False, False)

def equate(event):
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

def click(event):
    info1 = f"Coordinates: x={event.x}, y={event.y}\n"
    info2 = f"Widget: {event.widget}\n"
    messagebox.showinfo("What is in the event?", info1 + info2)

#def helper_a(event):
#    messagebox.showinfo("", "Enter a number a")

# def helper_b(event):
#     messagebox.showinfo("", "Enter a number b")

# def helper_c(event):
#     messagebox.showinfo("", "Enter a number c")

def helper_txt(event):
    messagebox.showinfo("", "Output")

def clean(event):
    event.widget.delete(0, END)

frame = LabelFrame(text="Enter initial data")
entry_a = Entry(frame, width=5)
label = Label(frame, text="x² +")
entry_b = Entry(frame, width=5)
label2 = Label(frame, text="x+")
entry_c = Entry(frame, width=5)
label3 = Label(frame, text="= 0")
frame2 = LabelFrame(text="Solution")
output = Text(frame2, width=30, height=10)
# button = Button(text="Solve Equation", command=equate)

frame.pack()
entry_a.pack(side="left")
label.pack(side="left")
entry_b.pack(side="left")
label2.pack(side="left")
entry_c.pack(side="left")
label3.pack(side="left")
frame2.pack()
output.pack()
# button.pack()

# entry_a.bind("<F1>", helper_a)
entry_a.bind("<F1>", lambda event: messagebox.showinfo("", "Enter a number a"))
entry_b.bind("<F1>", lambda event: messagebox.showinfo("", "Enter a number b"))
entry_c.bind("<F1>", lambda event: messagebox.showinfo("", "Enter a number c"))
output.bind("<F1>", helper_txt)

entry_a.bind("<FocusIn>", clean)
entry_b.bind("<FocusIn>", clean)
entry_c.bind("<FocusIn>", clean)

window.bind("<Control-Key-1>", lambda event: entry_a.focus())
window.bind("<Control-Key-2>", lambda event: entry_b.focus())
window.bind("<Control-Key-3>", lambda event: entry_c.focus())
window.bind("<Return>", equate)
window.bind("<Double-Button-1>", click)
window.mainloop()