from tkinter import *

window = Tk()
window.geometry("400x250")
window.title("Widgets and their positioning")

frame1 = Frame(bg="#7a249c")
frame2 = Frame(bg="#7a249c")

frame1.pack()
frame2.pack()

label1 = Label(frame1, justify=CENTER, relief=FLAT, font="raleway", bd=5, bg="#7a249c", fg="lime green", text="wWfcyvgbuhnjkmxdrcftvgybhj, fgcvhbjnknhb\nugyftcdxfcgvhbjn, xdcfn\nvgbhdtcfvy\nghbj fghsrdfgh\n")
label1.grid(column=0, row=0)

button1 = Button(frame2, text="Button 1", state=DISABLED, width=11)
button2 = Button(frame2, text="Button 2", width=11)

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)

window.mainloop()