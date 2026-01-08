# number = float(input("Number: "))
# numbers = 0
# sum1 = number

# while number != 0:
#     number = float(input("Number: "))
#     sum1 += number
#     numbers += 1
# average = sum1 / numbers
# print(average)

numbers = 0
sum1 = 0

while True:
    number = float(input("Number: "))
    if number == 0:
        break
    sum1 += number
    numbers += 1
average = sum1 / numbers
print(average)