with open("lesson-40/pangrams.txt") as file:
    text = file.read()
    text = text.replace("\n", " ")
print(text.count(" ") + 1)