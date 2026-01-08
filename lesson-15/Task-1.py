elems = input().split()
no_pairs = True

for i in range(len(elems) - 1):
    if elems[i].isalpha() and elems[i + 1].isalpha():
        no_pairs = False
        print(elems[i], elems[i + 1])
if no_pairs:
    print("Not enough words!")