def moving(list1):
    list1 = [*list1[2:], *list1[0:2]]
    return list1
print(moving([int(i) for i in input().split()]))