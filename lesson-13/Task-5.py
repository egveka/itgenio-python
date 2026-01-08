names = input().split()

for name in names:
    if name[0].lower() in "aeyuio":
        print(name)