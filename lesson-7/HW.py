# Write a program that forms a string of 10 characters. There should be random letters  at even index, and numbers at odd ones.
from random import choice

s = "qwertyuiopasdfghjklzxcvbnm"
s_num = "1234567890"
counter = 0
result = ""

while counter < 10:
    if counter % 2 != 0:
        result += choice(s_num)
    else:
        result += choice(s)
    counter += 1
print(result)