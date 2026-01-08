from tkinter import*

window = Tk()
window.geometry("550x300")
window.title("Color picker")
window.resizable(False, False)

def color_generate(value):
    red = red_scale.get()
    blue = blue_scale.get()
    green = green_scale.get()
    text_color = f"#{(255-red):02x}{(255-green):02x}{(255-blue):02x}"
    color = f"#{red:02x}{green:02x}{blue:02x}"
    label_color.config(bg=color, text=color, fg=text_color)
    entry_color.delete(0, END)
    entry_color.insert(END, color)


frame_RGB = LabelFrame(height=250, width=250, text="Choose colors")
frame_color = LabelFrame(height=250, width=250, text="Result color")
label_color = Label(frame_color, font=("Arial", 15, "bold"), height=8, width=16, text="")
entry_color = Entry(frame_color, font=("Arial", 15, "bold"))
red_scale = Scale(frame_RGB, label="Red",from_=0, to=255, orient="horizontal", width=20, length=200, fg="red", activebackground="red", command=color_generate)
blue_scale = Scale(frame_RGB, label="Blue",from_=0, to=255, orient="horizontal", width=20, length=200, fg="blue", activebackground="blue", command=color_generate)
green_scale = Scale(frame_RGB, label="Green",from_=0, to=255, orient="horizontal", width=20, length=200, fg="green", activebackground="green", command=color_generate)

frame_RGB.place(x=10, y=10)
frame_color.place(x=290, y=10)
label_color.place(x=50, y=40)
red_scale.place(x=10, y=0)
green_scale.place(x=10, y=150)
blue_scale.place(x=10, y=75)
entry_color.place(x=20, y=200)

window.mainloop()