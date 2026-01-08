import time
from random import choice

print("Typing speed check, write the phrase after appearing as fast as you can!")
phrases = ["Actions can speak louder than words.", 
           "Dont judge the book by its cover.", 
           "Early bird catches a worm.", 
           "Beauty is the eye of the beholder."
          ]

print("Ready...")
time.sleep(2)
print("Set...")
time.sleep(1)
print("Go!")
random_phrase = choice(phrases)
print(random_phrase)

start_time = time.time()
user_phrase = input()
end_time = time.time()

user_time = end_time - start_time

print(f"You've typed {len(user_phrase)} characters in {round(user_time, 3)} seconds.")
print(f"it means that your typing speed is {round(len(user_phrase) / user_time, 2)} characters per second.")

if user_phrase != random_phrase:
    print("You've made at least 1 mistake!")
else:
    print("No mistakes!")