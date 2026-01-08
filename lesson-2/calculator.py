print("Calculator")

user_number1 = float(input())
user_number2 = float(input())
user_math_sign = input()

sum = user_number1 + user_number2
product = user_number1 * user_number2
minus_sum = user_number1 - user_number2


if user_math_sign == "/" and user_number2 != 0:
    print(user_number1 / user_number2)
elif user_math_sign == "+":
    print(sum)
elif user_math_sign == "*":
    print(product)
elif user_math_sign == "-":
    print(minus_sum)
else:
    print("Error")
