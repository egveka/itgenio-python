from random import randint

rows = int(input("Amount of rows: "))
places = int(input("Amount of places in a row: "))

hall = []
for i in range(rows):
    row = []
    for j in range(places):
        number = randint(0, 1)
        row.append(number)
    hall.append(row)

occupied = 0
free = 0

for row in hall:
    print(*row)

for row in hall:
    for place in row:
        if place == 0:
            free += 1
        else:
            occupied += 1

print(f"Amount of free seats: {free}")
print(f"Amount of occupied seats: {occupied}")

sit_row = int(input("which row do you want to sit in? "))
sit_place = int(input("Which place do you want to sit in? "))

if hall[sit_row][sit_place] == 0:
    print("Your place has been booked!")
    hall[sit_row][sit_place] = 1
else:
    print("The place is occupied!")

for row in hall:
    print(*row)