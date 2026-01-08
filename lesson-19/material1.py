from tkinter import *

# Window's settings
window = Tk()
window.geometry("450x250")
window.title("New program")
window.maxsize(500, 300)
window.minsize(300, 200)
window.resizable(True, False)

# Widgets
close = Button(text="click me!!!", width=20, command=quit)
close.pack(expand=True)

# End of the program
window.mainloop()