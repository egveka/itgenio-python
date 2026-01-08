fr = int(input())
to = int(input())

# for i in range(fr, to + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

for i in range(fr, to + 1):
    div3 = i % 3 == 0
    div5 = i % 5 == 0
    if div3 or div5:
        if div3:
            print("Fizz", end="")
        if div5:
            print("Buzz",end="")
        print()
    else:
        print(i)