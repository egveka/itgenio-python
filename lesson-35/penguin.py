from tkinter import *

window = Tk()
window.geometry("320x320")
window.title("Penguin")
window.resizable(False, False)

canvas = Canvas(height="300", width="300", relief=SOLID, bd=1, bg="white")
canvas.pack()

body_black = canvas.create_oval(60, 80, 260, 280, outline="black", fill="black")
body_grey = canvas.create_oval(80, 140, 240, 250, outline="light gray", fill="light grey")
body_white = canvas.create_oval(100, 140, 220, 250, outline="white", fill="white")

eye_left = canvas.create_oval(120, 90, 160, 140, outline="white", fill="white")
eye_ball_left = canvas.create_oval(140, 100, 155, 120, outline="black", fill="black")
eye_right = canvas.create_oval(160, 100, 210, 130, outline="white", fill="white")
eye_ball_right = canvas.create_oval(165, 120, 173, 110, outline="black", fill="black")

foot_left = canvas.create_oval(70, 250, 160, 290, outline="orange", fill="orange")
foot_right = canvas.create_oval(165, 250, 255, 290, outline="orange", fill="orange")

beak = canvas.create_polygon(130, 140, 190, 140, 160, 180, outline="yellow", fill="gold")

wing_left = canvas.create_polygon(70, 140, 70, 170, 30, 170, outline="black", fill="black")
wing_right = canvas.create_polygon(250, 140, 250, 170, 295, 170, outline="black", fill="black")

blink_left = canvas.create_rectangle(120, 110, 160, 120, fill="white", outline="white", state="hidden")
blink_right = canvas.create_rectangle(165, 110, 200, 120, fill="white", outline="white", state="hidden")

def do_steps(event):
    key = event.keysym
    if key == "Left":
        canvas.move(foot_left, 0, -5)
        canvas.move(foot_right, 0, 5)
        canvas.move(wing_left, 0, 5)
        canvas.move(wing_right, 0, -5)
    
    if key == "Right":
        canvas.move(foot_right, 0, -5)
        canvas.move(foot_left, 0, 5)
        canvas.move(wing_right, 0, 5)
        canvas.move(wing_right, 0, 5)
        canvas.move(wing_left, 0, -5)

def blink(event):
    canvas.itemconfig(eye_ball_left, state="hidden")
    canvas.itemconfig(eye_left, state="hidden")
    canvas.itemconfig(eye_ball_right, state="hidden")
    canvas.itemconfig(eye_right, state="hidden")

    canvas.itemconfig(blink_left, state="normal")
    canvas.itemconfig(blink_right, state="normal")

def unblink(event):
    canvas.itemconfig(eye_ball_left, state="normal")
    canvas.itemconfig(eye_left, state="normal")
    canvas.itemconfig(eye_ball_right, state="normal")
    canvas.itemconfig(eye_right, state="normal")

    canvas.itemconfig(blink_left, state="hidden")
    canvas.itemconfig(blink_right, state="hidden")

canvas.bind_all("<KeyPress-a>", blink)
canvas.bind_all("<KeyPress-z>", unblink)
canvas.bind_all("<Key>", do_steps)

window.update()
window.mainloop()