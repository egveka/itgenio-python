num = int(input())

for i in range(num):
    s = input() 
    if "cat" in s.lower():
        print("MEOW")
        break
else:
    print("NO")