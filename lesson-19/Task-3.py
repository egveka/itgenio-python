def average(*numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    mean = sum / len(numbers)
    return mean
print(average(4, 5, 3))