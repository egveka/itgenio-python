from tkinter import *

window = Tk()
window.geometry("300x500")
window.title("Password Generator")
window.resizable(False, False)

lf = LabelFrame(text="Birthday")

l_d = Label(lf, text="Enter day")
l_m = Label(lf, text="Enter month")
e_d = Entry(lf)
e_m = Entry(lf)
button = Button(lf, text="Define Sign")

name = Label(text="Firstly enter birthday")
gif = PhotoImage(file="Zodiacs/img/start.gif")
image = Label(image=gif)

zodiac_names = ["Wrong date of birth!", "Capricorn", "Aquarius", "Pisces", "Aries",
                "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
                "Sagittarius"]

zodiac_files = ["start.gif", "capricon.gif", "aquarius.gif", "pisces.gif", "aries.gif",
                "taurus.gif", "gemeni.gif", "cancer.gif", "leo.gif", "virgo.gif",
                "libra.gif", "scorpio.gif", "sagittarius.gif"]

lf.pack()
l_d.pack()
e_d.pack(anchor=E)
l_m.pack()
e_m.pack(anchor=E)
button.pack()

name.pack()
image.pack()