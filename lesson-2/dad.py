counter = 1
amount = 0

while True:
    if counter > 10:
           break
    if counter % 2 != 0:
        # print(counter)
        amount += counter
    counter += 1
print("the sum of all even numbers from 1 to 10 =", amount)