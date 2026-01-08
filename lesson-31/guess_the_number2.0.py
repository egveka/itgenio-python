from random import randint

print("Welcome to Guess The Number! Game rules: The computer has thought of a number.\n"
       "You need to guess the number in 3 attempts. Good luck finding it!")

number = randint(1, 5)
user_guess = 0
attempts = 0

while user_guess != number:
    try:
        user_guess = int(input())
        attempts += 1
        if number > user_guess:
            print("Think bigger")
        elif number < user_guess:
            print("Think smaller")
        else:
            print("Congrats! You found it in", attempts, "attempts!")
            break
        if attempts == 3:
            print("The number was", number, "but you used your 3 attempts and didn't guess it,\n"
              "that means that you lost!")
            break
    except ValueError:
        print("Enter a 𝒏𝒖𝒎𝒃𝒆𝒓")