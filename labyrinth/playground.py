from tkinter import *
import levels

window = Tk()
window.geometry("500x500")
window.title("Labyrinth")
window.resizable(False, False)

canvas = Canvas(width=450, height=450, relief=SOLID, bg="white")
canvas.pack()

walls = []
doors = []
keys = []
exits = []
players = []
secrets = []
lava_pl = []

def createLevel(level):
    walls.clear()
    doors.clear()
    keys.clear()
    exits.clear()
    players.clear()
    secrets.clear()
    lava_pl.clear()
    x = 0
    y = 0
    side = 25
    for line in level:
        for block in line:
            if block == "W":
                wall = canvas.create_rectangle(x, y, x+side, y+side, fill="black", outline="black")
                walls.append(wall)
            if block == "K":
                key = canvas.create_rectangle(x, y, x+side, y+side, fill="yellow", outline="black")
                keys.append(key)
            if block == "D":
                door = canvas.create_rectangle(x, y, x+side, y+side, fill="red", outline="black")
                doors.append(door)
            if block == "E":
                exit = canvas.create_rectangle(x, y, x+side, y+side, fill="orange", outline="black")
                exits.append(exit)
            if block == "P":
                player = canvas.create_rectangle(x+1, y+1, x+side-1, y+side-1, fill="blue", outline="black")
                players.append(player)
            if block == "S":
                secret = canvas.create_rectangle(x, y, x+side, y+side, fill="black", outline="black")
                secrets.append(secret)
            if block == "L":
                lava = canvas.create_rectangle(x, y, x+side, y+side, fill="orange", outline="red")
                lava_pl.append(lava)
            x += side
        y += side
        x = 0

if __name__ == "__main__":
    createLevel(levels.level1)
    window.mainloop()