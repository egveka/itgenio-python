# file = open("lesson-40/pangrams.txt")
# text = file.read()
# file.close()

# print(text)

# file = open("lesson-40/pangrams.txt")
# text = file.read(10)
# text1 = file.read(10)
# file.close()

# print(text, text1)

# file = open("lesson-40/pangrams.txt")
# text = file.read(10)
# text1 = file.read(10)
# text2 = file.read()
# file.close()

# print(text, text1, text2)

with open("lesson-40/pangrams.txt") as file:
    text = file.readlines()
print(text)