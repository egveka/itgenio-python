from tkinter import *
from random import randint, choice

window = Tk()
window.geometry("500x500")
window.title("Canvas")
window.resizable(False, False)

canvas = Canvas(height=450, width=450, relief="solid", bg="white")
canvas.pack(padx=5, pady=5)

colors = ["red", "green", "blue", "yellow", "black", "magenta", "lime", "pink", "white", "orange"]
for i in range(2000):
    color = choice(colors)
    x = randint(-10, 500)
    y = randint(-10, 500)
    side = randint(10, 150)
    canvas.create_oval(x, y, x+side, y+side, fill=color, outline="black", width=3)
    window.update()
window.mainloop()