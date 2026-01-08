print("Are you over ten years old?")

user_answer = input()

if user_answer == "Yes" or user_answer == "yes":
    print("Specify your age")
    user_answer_2 = int(input())
    if user_answer_2 > 10:
        print("Access granted !")
    else:
        print("No access")
else:
    print("No access")