print("How are you?")

user_answer = input()
user_answer_2 = input()

if user_answer.lower() in ["good", "great"]:
    print("Nice, I'm fine too :)")
elif user_answer.lower() in ["bad", "horrible"]:
    print("Don't worry, everything will be fine soon.")
else:
    print("?")