s = "my name's Amad"
print("There are", s.count("a", 0, 1), "a's in first word")
if "a" in s[3:8]:
    print(s.replace("a", "A"))
else:
    print("error")
print("The length of the third word is", len(s[10:13]))