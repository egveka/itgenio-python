_set1 = set(input().split())
_set2 = set(input().split())

print(_set1)
print(_set2)

counter = 0
for s in _set1:
    if s in _set2:
        counter += 1
print(counter)