from tkinter import*

window = Tk()
window.geometry("200x500")
window.title("Rainbow")
window.resizable(False, False)

codes = ["#FF0000", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#000080", "#4B0082"]
colors = ["red", "orange", "yellow", "green", "light-blue", "blue", "purple"]

def change_text(index):
    color_name.config(text=colors[index])
    color_code.config(text=codes[index])


color_name = Label(font=("Arial", 14), bg="#ffffff", width=20, height=2)
color_name.pack(padx=5, pady=5)
color_code = Label(font=("Arial", 14), bg="#ffffff", width=20, height=2)
color_code.pack(padx=5, pady=5)
for i in range(7):
    button = Button(width=25, height=2, text=colors[i], command=lambda index=i: change_text(index))
    button.pack(padx=5, pady=5)

window.mainloop()