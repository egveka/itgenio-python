# file = open("lesson-40/pangrams.txt")
# text = file.read()
# file.close()

# print(text)

# file = open("lesson-40/pangrams.txt")
# text = file.read(92)
# # text1 = file.read(10)
# file.close()

# print(text)

# file = open("lesson-40/pangrams.txt")
# text = file.read(10)
# text1 = file.read(10)
# text2 = file.read()
# file.close()

# print(text, text1, text2)

# with open("lesson-40/pangrams.txt") as file:
#     text = file.readlines()
# print(text)

# with open("lesson-40/pangrams.txt", 'r') as file:
#     text = file.readlines()
# print(text)

# with open("lesson-40/numbers.txt", 'w') as file:
#     file.write("1")
#     file.write("2")
#     file.write("3")

# with open("lesson-40/numbers.txt", 'w') as file:
#     print("4", file=file)
#     print("5", file=file)
#     print("6", file=file)

# with open("lesson-40/numbers.txt", 'x') as file:
#     print("4", file=file)
#     print("5", file=file)
#     print("6", file=file)

with open("lesson-40/numbers.txt", 'a') as file:
    print("1000000", file=file)