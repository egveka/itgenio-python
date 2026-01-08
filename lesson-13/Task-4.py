num = [int(i) for i in input().split()]
sum1 = 1

for i in range(len(num)):
    sum1 *= num[i]
print(sum1)