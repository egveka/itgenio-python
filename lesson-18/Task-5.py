from random import randint

def detect_lucky(num):
    l = list(str(num))
    sum1 = 0
    sum2 = 0
    for i in range(len(l) - 3):
        sum1 += int(l[i])
    for j in range(3, len(l)):
        sum2 += int(l[j])
    if sum1 == sum2:
        return True
    else:
        return False
counter = 0
def get_lucky():
    global counter
    counter += 1
    num = randint(100000, 999999)
    if detect_lucky(num) == True:
        return num
    else:
        return get_lucky()

print(get_lucky())
print(counter)