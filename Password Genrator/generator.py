from random import choice
from random import shuffle

def generate_password(lowercase, number, special, uppercase):
    password = []
    lowercase_letters = "absdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    specials = "!@#$%^&*():;|\/><,.~`±§-_"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lowercase == True:
        for _ in range(4):
            password.append(choice(lowercase_letters))
    if number == True:
        for _ in range(4):
            password.append(choice(numbers))
    if special == True:
        for _ in range(4):
            password.append(choice(specials))
    if uppercase == True:
        for _ in range(4):
            password.append(choice(uppercase_letters))
    shuffle(password)
    new_password = "".join(password)
    return new_password
# print(generate_password(True, True))