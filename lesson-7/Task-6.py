s = input().replace(" ", "")


if s.lower() == s.lower()[::-1]:
    print("Yes")
else:
    print("No")