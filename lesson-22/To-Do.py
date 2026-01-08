from tkinter import*
from tkinter import filedialog

window = Tk()
window.geometry("400x550")
window.title("To-Do list")
window.resizable(False, False)

counter = 1
def add():
    global counter
    text = f"{counter}. {what.get()}\t\t{when.get()}\n"
    todolist.insert(END, text)
    what.delete(0, END)
    when.delete(0, END)
    counter += 1

def delete_button():
    todolist.delete(0.0, END)

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title="Save file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    if file:
        file.write(text)

def load():
    todolist.delete(0.0, END)
    file = filedialog.askopenfile(title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    text = file.read()
    todolist.insert(0.0, text)

labelframe1 = LabelFrame(text="Write down an important task")
label1 = Label(labelframe1, text="Task")
label2 = Label(labelframe1, text="Until when")
what = Entry(labelframe1)
when = Entry(labelframe1)
todolist = Text(width=35)
button1 = Button(text="Create new important task", command=add)
button2 = Button(text="Delete all tasks", command=delete_button)
save1 = Button(text="Save", command=save)
load1 = Button(text="Load", command=load)

labelframe1.pack()
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
what.grid(row=1, column=0)
when.grid(row=1, column=1)
button1.place(x=100, y=70)
todolist.place(x=80, y=100)
button2.place(x=135, y=420)
save1.place(x=165, y=447)
load1.place(x=165, y=475)

window.mainloop(0)