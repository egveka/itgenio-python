sum_ = 0
count = 0

for i in range(10):
    num = int(input())
    if num % 3 == 0:
        count += 1
        sum_ += num
if count == 0:
    print("0")
else:
    print(sum_ / count)