from random import randint

# keys = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         ["*", 0, "#"]]
# print(keys)
# print(keys[0][1], end=" ")
# print(keys[2][2], end=" ")
# for row in keys:
#     print(*row)
    # for column in row:
    #     print(column)

n = int(input("Amount of lines: "))
m = int(input("Amount of elements in a line: "))

array = []
for i in range(n):
    row = []
    for j in range(m):
        number = randint(1, 9)
        row.append(number)
    array.append(row)

for row in array:
    print(*row)