# As you know, when we come up with a password to an email account, certain complexity requirements 
# are often placed on this password.
# Write a program that simulates a password check, invented by the user. 
# The user enters a few words: the password and then password for confirmation.

# If the entered pair does not satisfy one of the following conditions, 
# the user enters the pair of passwords again, and so on until all the conditions 
# are fulfilled ( until the program displays “OK”).
#
# if the first password of the pair is long enough, but it contains a combination of characters "123", 
# the program displays the word "Simple!" and reads a couple of passwords again;
#
# if the previous checks are successful, but the entered passwords do not match, 
# the program displays the word "Different." and again reads a couple of passwords;
#
# if the second check is successful, the program displays "OK" and ends its work.

password1 = ""
password2 = ""

while True:
    password1 = input("Enter your password\n")
    password2 = input("Confirm your password\n")
    if password2 != password1:
        print("Different")
    elif "123" in password1:
        print("Simple!")
    else:
        print("OK")
        break

