print("Enter a number:")

user_number = int(input())

if user_number % 2 == 0 and user_number % 3 == 0 and user_number % 5 == 0:
    print("2, 3 and 5")
elif user_number % 2 == 0 and user_number % 3 == 0:
    print("2 and 3")
elif user_number % 2 == 0:
    print("2")
elif user_number % 3 == 0:
    print("3")
elif user_number % 5 == 0:
    print("5")
elif user_number % 2 == 0 and user_number % 5 == 0:
    print("2 and 5")
elif user_number % 3 == 0 and user_number % 5 == 0:
    print("3 and 5")
else:
    print("0")