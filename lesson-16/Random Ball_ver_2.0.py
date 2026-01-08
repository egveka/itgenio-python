from random import choice
import random

# printing out the rules
print("""Welcome to the "Random Ball" game!
Game rules: There are 5 green balls and 1 white ball in the bag. 
Players take turns pulling out one ball from the bag.
If the player pulled out a green ball - the game continues,
if the player pulled a white ball, then they lost and the game ends. 
Good luck!""")

# setting the variables
players = []
marbles = ["green", "green", "green", "green", "green", "white", "red"]
player_counter = int(input("Number of players: "))

# checking if there are less than or equal to 3 players
while player_counter > 3:
    player_counter = int(input("Maximum number of players is 3!\n"))

# inputing the name of the player
for i in range(player_counter):
    players.append(input(f"Enter the name of the player #{i + 1}: "))

# setting the main loop variables
current_player = 0
taken = 0

# main loop
while taken < 7:
# reseting the players when players are max
    if current_player == len(players):
        current_player = 0
# the turn of a player
    print(f"\nTurn: {players[current_player]}")
    input("Press Enter")
# if case with the result
    choosen_marble = choice(marbles)
    if choosen_marble == "white":
        print("White!")
        print(f"Player {players[current_player]} just lost!!!")
        break
    elif choosen_marble == "red":
        print("Red!")
        print(f"Player {players[current_player]} is eliminated")
        players.remove(players[current_player])
        random.shuffle(marbles)
        player_counter -= 1
        if player_counter == 1:
            break
        continue
    else:
        print("Green!")
        print("All good, continue")
# doing some variable changes
    marbles.remove(choosen_marble)
    current_player += 1
    taken += 1