from tkinter import *

window = Tk()
window.geometry("700x600")
window.title("Snake game")
window.resizable(False, False)

WIDTH = 700
HEIGHT = 600
IN_GAME = True

c = Canvas(window, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
c.focus_set()

class Segment:
    def __init__(self,x,y,SEG_SIZE):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y + SEG_SIZE, fill="white")
s1 = Segment(0, 50, 50)
s2 = Segment(50, 50, 50)
s3 = Segment(100, 50, 50)
# s4 = Segment(150, 50, 50)
# s5 = Segment(200, 50, 50)
# s6 = Segment(250, 50, 50)
# s7 = Segment(300, 50, 50)
# s8 = Segment(350, 50, 50)
# s9 = Segment(400, 50, 50)
# s10 = Segment(450, 50, 50)
# s11 = Segment(450, 100, 50)
# s12 = Segment(450, 150, 50)
# s13 = Segment(450, 200, 50)
# s14 = Segment(450, 250, 50)
# s15 = Segment(450, 300, 50)
# s16 = Segment(500, 300, 50)
# s17 = Segment(550, 300, 50)
# s18 = Segment(600, 300, 50)
# s19 = Segment(650, 300, 50)

seg_list = [s1, s2, s3]

window.mainloop()