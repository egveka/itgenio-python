from random import choice

# num_of_rounds = int(input("Enter the number of rounds: "))
# defeated_by = {"rock":"scissors", "scissors":"paper", "paper":"rock"}
# user_choice = input("Choose an element(rock, paper or scissors): ")
# comp_choice = choice(list(defeated_by.keys()))

# print(comp_choice)
# for i in range(num_of_rounds):
#     print(f"Round {i+1}")

#     user_choice = input("Choose an element(rock, paper or scissors): ")
#     comp_choice = choice(list(defeated_by.keys()))
#     print(comp_choice)

#     for key,value in defeated_by.items():
#         if user_choice == key and comp_choice == value:
#             print("You win!\n")
#             break
#         elif user_choice == value and comp_choice == key:
#             print("You lose!\n")
#             break
#     else:
#         print("It's a draw!\n")

num_of_rounds = int(input("Enter the number of rounds: "))
defeated_by = {"rock":"scissors", "scissors":"paper", "paper":"rock"}

win_counter = 0
draw_counter = 0
lose_counter = 0
round_counter = 0

while round_counter != num_of_rounds:
    print(f"Round {round_counter + 1}")

    user_choice = input("Choose an element(rock, paper or scissors): ")
    comp_choice = choice(list(defeated_by.keys()))
    print(comp_choice)

    for key,value in defeated_by.items():
        if user_choice == key and comp_choice == value:
            print("You win!\n")
            round_counter += 1
            win_counter += 1
            break
        elif user_choice == value and comp_choice == key:
            print("You lose!\n")
            round_counter += 1
            lose_counter += 1
            break
    else:
        print("It's a draw!\n")
        draw_counter += 1

print(f"Wins: {win_counter}, Draws: {draw_counter}, Loses: {lose_counter}")