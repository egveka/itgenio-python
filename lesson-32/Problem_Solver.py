from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("550x300")
window.title("Problem Solver")
window.resizable(False, False)

def equate():
    try:
        solution = eval(equasion.get())
        messagebox.showinfo("Done!", f"Solution was found: {solution}")
    except NameError:
        messagebox.showerror("Attention!", "You wrote something 𝒄𝒐𝒎𝒑𝒍𝒆𝒕𝒆𝒍𝒚 incorrect!")
    except SyntaxError:
        messagebox.showerror("Error!", "You forgot something, revise the example!")
    except ZeroDivisionError:
        messagebox.showerror("Are you serious?", "Are you seriously dividing by zero?")

frame = Frame()
label = Label(frame, text="Enter an equasion using those signs:\n + - * / // % **", anchor="center")
equasion = Entry(frame)
equasion.focus()
button = Button(frame, text="Solve", command=equate)

frame.pack()
label.pack()
equasion.pack()
button.pack()

window.mainloop()