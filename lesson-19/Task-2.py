def exam(limit, *grades):
    counter = 0
    for i in range(len(grades)):
        if grades[i] >= limit:
            counter += 1
    return f"{counter} students passed the exam."
print(exam(3, 2, 3, 4, 5, 1))