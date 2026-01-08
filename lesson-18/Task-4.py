def sum_of_digits(n):
    l = list(str(n))
    sumsum = 0
    for i in range(len(l)):
        sumsum += int(l[i])
    return sumsum



first_digit = int(input("First number is: "))
second_digit = int(input("Second number is: "))

print(sum_of_digits(first_digit))
print(sum_of_digits(second_digit))

if sum_of_digits(first_digit) > sum_of_digits(second_digit):
    print(f"Sum of the numbers {first_digit} is greater!")
elif sum_of_digits(second_digit) > sum_of_digits(first_digit):
    print(f"Sum of the numbers {second_digit} is greater!")
else:
    print("All of the sums are equall!")