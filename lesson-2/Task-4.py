counter = 1
amount = 1

while True:
    if counter > 10:
           break
    if counter % 2 == 0:
        # print(counter)
        amount *= counter
    counter += 1
print("the product of all even numbers from 1 to 10 =", amount)