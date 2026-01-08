s = input()

num_of_A = s.lower().find("a")
num_of_B = s.lower().find("b")

if num_of_A > num_of_B and num_of_B >= 0:
    print("B")
elif num_of_A < num_of_B and num_of_A >= 0:
    print("A")
else:
    print("error")