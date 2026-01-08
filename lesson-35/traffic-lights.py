from tkinter import *

window = Tk()
window.geometry("300x350")
window.title("Traffic Light")
window.resizable(False, False)

canvas = Canvas(height=340, width=280, relief=SOLID, bd=1, bg="white")
canvas.pack()

canvas.create_rectangle(85, 10, 205, 290, fill="#4a4948", outline="black")
canvas.create_rectangle(135, 290, 155, 360, fill="#4a4948", outline="black")
canvas.create_rectangle(95, 20, 195, 280, fill="#818181")

red = canvas.create_oval(114, 40, 175, 100, fill="#e00202", outline="black")
yellow = canvas.create_oval(114, 120, 175, 180, fill="#fbff03", outline="black")
green = canvas.create_oval(114, 195, 175, 255, fill="#02e302", outline="black")

def reset():
    canvas.itemconfig(red, fill="#7a6161")
    canvas.itemconfig(yellow, fill="#abab90")
    canvas.itemconfig(green, fill="#97ad97")
    window.bind("<space>", red_light)

def green_light():
    canvas.itemconfig(yellow, fill="#abab90")
    canvas.itemconfig(green, fill="#02e302")
    window.after(2000, reset)

def yellow_light():
    canvas.itemconfig(red, fill="#7a6161")
    canvas.itemconfig(yellow, fill="#fbff03")
    window.after(2000, green_light)

def red_light(event):
    canvas.itemconfig(red, fill="#e00202")
    window.after(2000, yellow_light)
    window.unbind("<space>")

reset()
window.update()
window.mainloop()