num = 100

while num != -100:
    if num % 3 == 0:
        print(num, end=",")
    num -= 1

print("\n")

for i in range(100, -100, -1):
    if i % 3 == 0:
        print(i, end=",")