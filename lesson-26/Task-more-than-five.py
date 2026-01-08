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

for i in range(len(array)):
    for j in range(len(row)):
        if array[i][j] >= 5:
            array[i][j] = 0

for row in array:
    print(*row)