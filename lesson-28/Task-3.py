_list = input().split()
_set = set()

for t in _list:
    if t in _set:
        print("YES")
    else:
        print("NO")
        _set.add(t)