with open("lesson-40/evens.txt", "w") as file:
    res = ""
    for i in range(21):
        if i % 2 == 0:
            if i > 0:
                res += " "
            res += f"{i}"
    print(res, file=file)