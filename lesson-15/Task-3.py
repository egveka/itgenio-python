string = input()
phrase = input().split()

if string.find(phrase[0]) < string.find(phrase[1]):
    print("YES")
else:
    print("NO")