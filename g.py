import tkinter as tk
import time

WIDTH, HEIGHT = 600, 400
GRAVITY = 0.5
SPEED = 5

class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='skyblue')
        self.canvas.pack()

        # Player
        self.player = self.canvas.create_rectangle(50, HEIGHT-50-30, 80, HEIGHT-50, fill='green')
        self.vy = 0
        self.on_ground = True

        # Levels
        self.levels = [ [(300, HEIGHT-50-50, 30,50),(500, HEIGHT-50-50,30,50)],
                        [(250, HEIGHT-50-50,30,50),(400, HEIGHT-50-50,30,50)] ]
        self.level_index = 0
        self.obstacles = []
        self.setup_level()

        self.score = 0
        root.bind('<space>', self.jump)
        self.update_game()

    def setup_level(self):
        self.canvas.delete('obstacle')
        self.obstacles = []
        for ob in self.levels[self.level_index]:
            x,y,w,h = ob
            rect = self.canvas.create_rectangle(x,y,x+w,y+h, fill='red', tags='obstacle')
            self.obstacles.append(rect)
        self.canvas.coords(self.player,50, HEIGHT-50-30, 80, HEIGHT-50)
        self.vy = 0
        self.on_ground = True

    def jump(self, event):
        if self.on_ground:
            self.vy = -10
            self.on_ground = False

    def update_game(self):
        # Gravity
        if not self.on_ground:
            self.vy += GRAVITY
            self.canvas.move(self.player,0,self.vy)
            px1,py1,px2,py2 = self.canvas.coords(self.player)
            if py2 >= HEIGHT-50:
                self.canvas.move(self.player,0, HEIGHT-50 - py2)
                self.vy=0
                self.on_ground = True

        # Move obstacles
        for ob in self.obstacles:
            self.canvas.move(ob,-SPEED,0)

        # Collision
        px1,py1,px2,py2 = self.canvas.coords(self.player)
        for ob in self.obstacles:
            ox1,oy1,ox2,oy2 = self.canvas.coords(ob)
            if px1 < ox2 and px2 > ox1 and py1 < oy2 and py2 > oy1:
                print("Hit! Restarting level")
                self.setup_level()
                self.score = 0

        # Remove offscreen obstacles
        self.obstacles = [ob for ob in self.obstacles if self.canvas.coords(ob)[2] > 0]

        # Next level
        if not self.obstacles:
            self.level_index += 1
            if self.level_index >= len(self.levels):
                print("Finished all levels!")
                self.level_index = 0
            self.setup_level()

        # Score
        self.score += 1
        self.canvas.delete('score')
        self.canvas.create_text(50,20, text=f"Score: {self.score}", fill='white', font=('Arial',20), tags='score')

        self.root.after(20,self.update_game)

root = tk.Tk()
root.title("Geometry Dash Mini")
game = Game(root)
root.mainloop()