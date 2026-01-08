from tkinter import *

window = Tk()
window.geometry("600x500")
window.title("Widget positioning")

frame1 = LabelFrame(text="Pack", width=300, height=100)
frame1.place(x=90, y=330)

frame2 = LabelFrame(text="Grid", width=300, height=100)
frame2.place(x=150, y=130)

frame3 = LabelFrame(text="Place", width=400, height=100)
frame3.place(x=90, y=10)

button10 = Button(frame1, text="Button 10", bg="white", fg="black", width=10)
button11 = Button(frame1, text="Button 11", bg="white", fg="black", width=10)
button12 = Button(frame1, text="Button 12", bg="white", fg="black", width=10)

button10.pack(pady=5, padx=5, side=LEFT)
button11.pack(pady=5, padx=5, side=LEFT)
button12.pack(pady=5, padx=5, side=LEFT)

button20 = Button(frame2, text="Button 20", bg="white", fg="black", width=25)
button21 = Button(frame2, text="Button 21", bg="white", fg="black", width=10)
button22 = Button(frame2, text="Button 22", bg="white", fg="black", width=10, height=3)
button23 = Button(frame2, text="Button 23", bg="white", fg="black", width=10)
button24 = Button(frame2, text="Button 24", bg="white", fg="black", width=10)
button25 = Button(frame2, text="Button 25", bg="white", fg="black", width=10)

button20.grid(column=0, row=0, pady=5, padx=5, columnspan=2)
button21.grid(column=0, row=1, pady=5, padx=5)
button22.grid(column=1, row=1, pady=5, padx=5, rowspan=2)
button23.grid(column=0, row=2, pady=5, padx=5)
# button24.grid(column=1, row=2, pady=5, padx=5)
button25.grid(column=0, row=3, pady=5, padx=5)

button30 = Button(frame3, text="Button 30", bg="white", fg="black", width=10)
button31 = Button(frame3, text="Button 31", bg="white", fg="black", width=10)

button30.place(x=0, y=0)
button31.place(x=270, y=50)

window.mainloop()