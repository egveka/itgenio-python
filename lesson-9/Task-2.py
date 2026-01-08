for num in range(7, -6, -2):
    print(num, end=" ")

print()

_sum = 0
mult = 1
for n in range(1, 11):
   _sum += n
   mult *= n
print("sum =", _sum)
print("mult =", mult)