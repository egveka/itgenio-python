from tkinter import *
from tkinter import messagebox
from random import shuffle
from random import randint

root = Tk()
root.geometry("700x520+300+200")
root.configure(bg="#0B1C3D")

questions = [["What is the capital of China?", "Shanghai", "Chongquing", "Beijing", "Shezhen", "Beijing"], 
             ["What is the name of the unregistered animagus\n which was uncovered in book number 4?", "Peter Petigrew", "Sirius Black", "Rita Skeeter", "Proffesor Mcgonagall", "Rita Skeeter"],
             ["Which date is western christmas?", "24th December", "25th December", "26th December", "27th December", "25th December"],
             ["Who won the 2022 world cup?", "Brazil", "France", "Argentina", "Germany", "Argentina"],
             ["Which intervals are the olympics in?", "every 2 years", "every 3 years", "every year", "every 4 years", "every 4 years"],
             ["What is the continent New Zealand is in?", "Europe", "Asia", "Oceania", "North America", "Oceania"],
             ["Who invented the light bulb?", "Nikola Tesla", "Albert Einstein", "Alessandro Volta", "Thomas Edison", "Thomas Edison"],
             ["Which of the following languages has the\n longest alphabet in the world?", "Russian", "Hindi", "Japanese", "Khmer", "Khmer"],
             ["The fear of insects is known as what?", "Entomophobia", "Chilopodophobia", "Arachnophobia", "Ailurophobia", "Entomophobia"],
             ["In what country was the first paper money used?", "Greece", "China", "Turkey", "Iran", "China"],
             ["In what country are the Spanish Steps located?", "Spain", "Italy", "France", "Argentina", "Italy"],
             ["Who found gravity?", "Nicola Tesla", "Albert Einstein", "Isaac Newton", "Mozzart", "Isaac Newton"],
             ["How many colors are in the rainbow?", "6", "7", "8", "9", "7"],
             ["How many planets are in a solar system?", "6", "9", "8", "12", "8"],
             ["What sport is considered the oldest in the world?", "Wrestling", "Basketball", "Gymnastics", "Boxing", "Wrestling"],]

numQue = 0
btns = questions[numQue][1:15]
points = 0
counter = 0
c2 = 0

pic = PhotoImage(file="Who-Wants-To-Be-A-Millioner/wwtbam4.png")
picL = Label(root, image=pic)

queL = Label(root, text=questions[numQue][0], font='Verdana 22', bg="#0B1C3D", fg="#FFD700")
btn1 =Button(root, text=btns[0], font='Verdana 22', width=20,command=lambda: check(btns[0]), relief=RAISED, activeforeground="#FFD700")
btn2 =Button(root, text=btns[1], font='Verdana 22', width=20,command=lambda: check(btns[1]), relief=RAISED, activeforeground="#FFD700")
btn3 =Button(root, text=btns[2], font='Verdana 22', width=20,command=lambda: check(btns[2]), relief=RAISED, activeforeground="#FFD700")
btn4 =Button(root, text=btns[3], font='Verdana 22', width=20,command=lambda: check(btns[3]), relief=RAISED, activeforeground="#FFD700")
point_label = Label(root, text=f"Your Balance:\n{points}$", fg="#FFD700", font=("Arial", 30), bg="blue")

picL.grid(row=0, column=0, columnspan=1)
queL.grid(row=1, column=0, columnspan=2)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=3, column=0)
btn4.grid(row=3, column=1)
point_label.grid(row=0, column=1)

def check(otv):
    global numQue
    global points
    if otv == questions[numQue][5]:
        correct = messagebox.showinfo("Correct!", "Your answer is correct!")
        friend_answer.config(text="")
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        numQue += 1
        if numQue == 1 or numQue == 2 or numQue == 3:
            points += 100
        elif numQue == 4:
            points = 500
        elif numQue == 5 or numQue == 6 or numQue == 7 or numQue == 8 or numQue == 9 or numQue == 10 or numQue == 13 or numQue == 14:
            points *= 2
        elif numQue == 11:
            points = 61000
        elif numQue == 12:
            points = 125000
        point_label.config(text=f"Your Balance:\n{points}$")
        if numQue == 15:
            queL.config(text="You Won! You got 1,000,000$!", bg="green")
            btn1.destroy()
            btn2.destroy()
            btn3.destroy()
            btn4.destroy()
            point_label.destroy()
            root.geometry("350x350+300+200")
        else:
            btns = questions[numQue][1:5]
            shuffle(btns)
            queL.config(text=questions[numQue][0])
            btn1.config(text=btns[0], command=lambda: check(btns[0]))
            btn2.config(text=btns[1], command=lambda: check(btns[1]))
            btn3.config(text=btns[2], command=lambda: check(btns[2]))
            btn4.config(text=btns[3], command=lambda: check(btns[3]))
    else:
        mistake = messagebox.showinfo("Wrong!", "Your answer is wrong, you lost!")
        queL.config(text="You Lost! You lost all your money \n and you won't be getting the 1,000,000$!", bg="red")
        btn1.destroy()
        btn2.destroy()
        btn3.destroy()
        btn4.destroy()
        tip1.destroy()
        tip2.destroy()
        point_label.destroy()
        root.geometry("480x400+300+200")
        root.after(10000, root.destroy)

def chance():
        global counter
        counter += 1
        if counter <= 2:     
            if btn1.cget("text") != questions[numQue][5]:
                btn1.config(state="disabled")
                if btn2.cget("text") != questions[numQue][5]:
                    btn2.config(state="disabled")
                elif btn3.cget("text") != questions[numQue][5]:
                    btn3.config(state="disabled")
                elif btn4.cget("text") != questions[numQue][5]:
                    btn4.config(state="disabled")
            elif btn2.cget("text") != questions[numQue][5]:
                btn2.config(state="disabled")
                if btn3.cget("text") != questions[numQue][5]:
                    btn3.config(state="disabled")
                elif btn4.cget("text") != questions[numQue][5]:
                    btn4.config(state="disabled")
            elif btn3.cget("text") != questions[numQue][5]:
                btn3.config(state="disabled")
                if btn4.cget("text") != questions[numQue][5]:
                    btn4.config(state="disabled")
            elif btn4.cget("text") != questions[numQue][5]:
                    btn3.config(state="disabled")
        else:
            tip1.config(state="disabled")

def friend():
    global c2
    c2 += 1
    if c2 <= 2:
        if randint(1,100) <= 70:
            friend_answer.config(text=f"Friend's answer: {questions[numQue][5]}")
        else:
            friend_answer.config(text=f"Friend's answer: {questions[numQue][randint(1,4)]}")
    else:
        tip2.config(state="disabled")


tip1 = Button(text="50-50", command=chance, font=("Arial", 18), width=10, height=3)
tip1.grid(column=0)
    
tip2 = Button(text="Call a Friend", command=friend, font=("Arial", 18), width=10, height=3)
tip2.grid(row=4, column=1)
friend_answer = Label(text="", font=("Arial", 24), fg="#FFD700", bg="#0B1C3D")
friend_answer.grid()

root.mainloop()