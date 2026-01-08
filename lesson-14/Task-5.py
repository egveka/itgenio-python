numbers = [int(i) for i in input().split()]

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        print(numbers[i], end=" ")