s = input()

w1 = s[0:s.find(" ")]
w2 = s[s.find(" ") + 1 :s.rfind(" ")]
w3 = s[s.rfind(" ") + 1:] 

print("There are", w1.count("a"), "a's in the first word")
if "a" in w2:
    print(w2.replace("a", "A"))
else:
    print("Error")
print("The length of the third word is", len(w3))