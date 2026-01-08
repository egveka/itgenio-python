from random import choice

choice_number = 0
favorite_number = ""

while favorite_number.lower() != "yes":
    choice_number = choice ([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(choice_number)
    favorite_number = input("Is this your favorite number? ")