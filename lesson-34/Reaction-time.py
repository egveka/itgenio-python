from tkinter import *
from random import randint
import time

window = Tk()
window.geometry("500x500")
window.title("Canvas")
window.resizable(False, False)

canvas = Canvas(height=450, width=450, relief="solid", bg="white")
canvas.pack(padx=5, pady=5)

def restart():
    global y, counter, total_seconds
    y = 0
    counter = 0
    total_seconds = 0
    canvas.delete("all")
    window.after(5000, main)

y = 0
counter=0
total_seconds = 0
def click(event):
    global y, counter, total_seconds
    seconds = round(time.time() - start_time, 3)
    y+=20
    counter+=1
    total_seconds+=seconds
    score = canvas.create_text(30, y, font="Arial 14", text=seconds)
    canvas.delete(ball)
    if counter != 5:
        window.after(500, main)
    elif counter == 5:
        canvas.create_text(225, 225, anchor=CENTER, font="Arial 24", 
                           text=f"Your reaction time is: {round(total_seconds, 3)}")
        window.after(5000, restart)

def start():
    global start_time
    start_time = time.time()
    canvas.itemconfig(ball, fill="lime", outline="green")
    canvas.tag_bind(ball, "<Button-1>", click)

def main():
    global ball
    ball = canvas.create_oval(280, 280, 170, 170, fill="black", outline="black", width=3)
    ct = randint(3000, 7000)
    window.after(ct, start)

main()
window.mainloop()