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

for i in range(columns):
    _sum = 0
    for j in range(rows):
        _sum += array[j][i]
    print(_sum)