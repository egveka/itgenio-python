num = int(input())
counter = 0

for i in range(1, num + 1):
    if num % i == 0:
        counter += 1
        print(i)
if counter > 2:
    print("NO")
else:
    print("PRIME")