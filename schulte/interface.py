from tkinter import *
from tkinter import messagebox
from random import shuffle
import time


window = Tk()
window.geometry("700x500")
window.title("Schult")
window.resizable(False, False)

greeting_frame = Frame()

label = Label(greeting_frame, font=("Arial", 15), justify=LEFT, 
              text="Schulte is a simple game that helps improve\n" \
"peripheral vision, reading speed, and reaction time. The rules are:\n" \
"You need to click all the numbers from 1 to 9 in the correct order as fast as possible.\n" \
"If you make a mistake, the game restarts from the beginning.\n" \
"The winner is the player who completes the task the fastest.")

def restart():
    global numbers_in_order
    global game_frame
    greeting_frame.forget()
    numbers_in_order = ["1", "2", "3", "4", "5", "6", "7" ,"8", "9"]
    random_numbers = ["1", "2", "3", "4", "5", "6", "7" ,"8", "9"]
    shuffle(random_numbers)
    game_frame = Frame()
    game_frame.pack(anchor="center")
    row = 0
    column = 0
    for i in range(9):
        num_btn = Button(game_frame, font=("Arial", 18), width=8, height=3, 
                         text=random_numbers[i])
        num_btn.grid(row=row, column=column)
        if i == 2 or i == 5 or i == 8:
            row += 1
            column = 0
        else:
          column += 1
        num_btn.bind("<Button-1>", click)

def timer():
    global start
    ready = messagebox.askyesno("Are You Ready?", "After clicking ""Yes"" the time will start")
    if ready == True:
        start = time.time()
        restart()

button = Button(greeting_frame, text="Start the game", command=timer)

def start_over(event):
    ask = messagebox.askyesno("The question", "Do you want to start over?")
    if ask:
        game_frame.destroy()
        greeting_frame.pack(expand=True)
        greeting_frame.focus_force()

def click(event):
    global start
    window.bind("<Escape>", start_over)
    # print(event.widget)
    if event.widget["text"] == numbers_in_order[0]:
        event.widget.config(state=DISABLED)
        event.widget.unbind("<Button-1>")
        numbers_in_order.pop(0)
        if len(numbers_in_order) == 0:
            end = time.time()
            elapsed = end - start
            messagebox.showinfo("Nice!", f"You won, your time is {round(elapsed, 3)}! Want to try again?")
            game_frame.destroy()
            greeting_frame.pack(expand=True)
            greeting_frame.focus_force()
    else:
        mistake = messagebox.showerror("Oops", "You made a mistake! Starting over...")
        start = time.time()
        if mistake:
            game_frame.destroy()
            restart()

greeting_frame.pack()
label.pack()
button.pack()

window.mainloop()