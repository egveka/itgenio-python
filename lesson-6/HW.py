password = input("Enter your password\n")

valid = password.isalnum() and not password.isdigit() and not password.isalpha()

print(valid)