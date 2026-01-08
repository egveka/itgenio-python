dishes = input().split()

for dish in dishes:
    if dish[0].isupper():
        print(dish)