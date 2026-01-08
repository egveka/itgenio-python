num = int(input())
counter = 0

for i in range(num):
    s = input()
    if "cat" in s.lower():
        counter += 1

if counter > 0:
    print("MEOW")
else:
    print("NO")