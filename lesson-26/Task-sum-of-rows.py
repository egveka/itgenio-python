from random import randint

rows = randint(2, 5)
columns = randint(2, 5)

array = []
for i in range(rows):
    row = []
    for j in range(columns):
        num = randint(1,9)
        row.append(num)
    array.append(row)

for row in array:
    print(*row)

print()

for row in array:
    mean = 0
    for elem in row:
        mean += elem
    mean /= len(row)
    print(round(mean, 3))