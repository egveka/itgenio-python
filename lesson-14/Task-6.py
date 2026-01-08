from random import randint

n = int(input())
nums = []

for i in range(n):
    random_num = randint(1, 100)
    nums.append(random_num)
print(*nums)