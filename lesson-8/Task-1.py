s = input()

w1 = s[0:s.find(" ")]
w2 = s[s.rfind(" ") + 1 :]

if len(w1) >= len(w2):
    print(w1, w2)
else:
    print(w2, w1)