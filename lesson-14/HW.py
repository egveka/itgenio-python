list1 = input().split()
list2 = input().split()

for x in list1:
    if x in list2:
        print(x, end=" ")