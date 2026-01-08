from random import choice
import random

# printing out the rules
print("Welcome to the ""Random Ball"" game! Game rules: There are 5 green balls and 1 white ball in the bag. Players take turns pulling out one ball from the bag.\nIf the player pulled out a green ball - the game continues, if the player pulled a white ball, then they lost and the game ends. Good luck!😊😎")

# setting the variables
num_of_marbles = int(input("How much marbles do you want❓ "))
players = []
marbles = []
player_counter = int(input("How much players❓(it is more fun to play with 5+ people😉) "))

# adding the marbles
for i in range(num_of_marbles):
    if i == num_of_marbles - 1:
        if num_of_marbles >= 15:
            marbles.append("red")
            marbles.append("red")
        else:
            marbles.append("red")
    elif i == num_of_marbles - 2:
        if num_of_marbles >= 10:
            marbles.append("white")
            marbles.append("white")
    else:
        marbles.append("green")

# inputing the name of the player
for i in range(player_counter):
    players.append(input(f"Enter the name of the player #{i + 1}: "))

# setting the main loop variables
current_player = 0
taken = 0

# main loop
while taken < num_of_marbles:
# reseting the players when players are max
    if current_player == len(players):
        current_player = 0
# the turn of a player 
    print()
    print("Turn: ", players[current_player])
    input("Press Enter")
# if case with the result
    choosen_marble = choice(marbles)
    if choosen_marble == "white":
        print("White!")
        print(f"Player {players[current_player]} just lost!!!👎")
        break
    elif choosen_marble == "red":
        print("Red!")
        print(f"Player {players[current_player]} is eliminated!👎")
        players.remove(players[current_player])
        random.shuffle(marbles)
        if len(players) == 1:
            print("Congratulations, You won!!!")
            break
        continue
    else:
        print("Green!")
        print("All good, continue!👍")
# doing some variable changes
    marbles.remove(choosen_marble)
    current_player += 1
    taken += 1