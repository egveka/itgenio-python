from random import choice

colors = ["red", "green", "blue"]
roles = [0,1,2]
class Player():
    def __init__(self, username, role=None, color=None):
        self.username = username
    def choose_color(self):
        color = input(f"Choose the color, {colors}: ")
        if color not in colors:
            print("Invalid color")
        elif color in colors:
            print(f"Choosen color: {color}")
            self.color = color
            colors.remove(color)
    def choose_role(self):
        role = choice(roles)
        self.role = role
        if len(roles) == 0:
            print("All roles are given")
        else:
            if self.role == 0:
                print(f"{self.username} is the impostor")
                roles.remove(role)
            else:
                print(f"{self.username} is not the impostor")
                roles.remove(role)
player1 = Player("player1")
player2 = Player("player2")
player3 = Player("player3")
player4 = Player("p4")
# player1.choose_color()
# player2.choose_color()
# # print(player1.color)
# player1.choose_role()
# player2.choose_role()
# player3.choose_role()
# print(player1.role)
player1.choose_color()
player2.choose_color()
player3.choose_color()
player4.choose_color()