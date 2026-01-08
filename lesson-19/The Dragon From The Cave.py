import time
from random import choice

counter_win = 0
counter_lost = 0

def display_intro():
    print("You are in a land full of dragons. In front of you, you see two caves,")
    print("In one cave, the dragon is friendly and will share his treasure with you,")
    print("But the other dragon is greedy and hungry and wants to eat you.")
    print()

def choose_cave():
    cave = 0
    while cave != 1 and cave != 2:
        cave = int(input("Which cave do you want to enter?\n"))
    return cave

def check_cave(chosen_cave):
    global counter_lost, counter_win
    print("You are approaching a cave...")
    time.sleep(2)
    print("It's dark and creepy...")
    time.sleep(2)
    print("A large dragon jumps in front of you!")
    print("He opens his jaws and...")
    print()
    l = [1, 2]
    chance = choice(l)
    if chance != chosen_cave:
        print("The dragon eats you in one bite!")
        counter_lost += 1
    else:
        counter_win += 1
        print("The dragon gives you his treasure!")

continue_playing = "yes"

while True:
    if continue_playing.lower() != "yes":
        print("Ok")
        print(f"You have been eaten {counter_lost} times!")
        print(f"You have been given treasure {counter_win} times!")
        break
    elif continue_playing == "yes":
        display_intro()
        x = choose_cave()
        check_cave(x)
    continue_playing = input("Do you want to play(yes or no)?")