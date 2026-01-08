list1 = set(input().split())
list2 = set(input().split())

print(*list2.difference(list1))