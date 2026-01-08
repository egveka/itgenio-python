from playground import window
from playground import canvas
from playground import walls
from playground import keys
from playground import exits
from playground import doors
from playground import players
from playground import lava_pl
from playground import createLevel
from levels import levels

currentLevel = 0
createLevel(levels[currentLevel])

def playerMove(event):
    global currentLevel
    player = players[0]
    key2 = event.keysym
    x = 0 
    y = 0
    if key2 == "Up":
        y = -5
    if key2 == "Left":
        x = -5
    if key2 == "Right":
        x = 5
    if key2 == "Down":
        y = 5
    canvas.move(player, x, y)
    for wall in walls:
        x1, y1, x2, y2 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.move(player, -x, -y)
    for key1 in keys:
        x1, y1, x2, y2 = canvas.coords(key1)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete(key1)
            keys.remove(key1)
            if len(keys) == 0:
                for door in doors:
                    canvas.itemconfig(door, fill="green")
    for door in doors:
        if canvas.itemcget(door, "fill") == "red":
            x1, y1, x2, y2 = canvas.coords(door)
            if player in canvas.find_overlapping(x1, y1, x2, y2):
                canvas.move(player, -x, -y)
    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete("all")
            if currentLevel < 1:
                currentLevel += 1
                createLevel(levels[currentLevel])
            else:
                canvas.unbind_all("<Key>")
                canvas.create_text(200, 200, text="You Won!!!", font=("Arial", 48), fill="green")
                return
    for lava in lava_pl:
        x1, y1, x2, y2 = canvas.coords(lava)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete("all")
            createLevel(levels[currentLevel])

canvas.bind_all("<Key>", playerMove)

window.mainloop()