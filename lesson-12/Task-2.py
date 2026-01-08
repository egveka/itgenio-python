capitals = input("Enter capitals: ").split()
print(capitals)

new_capital = input("Enter another one: ")
capitals.append(new_capital)
print(capitals)

for i in range(len(capitals) - 1, -1 , -1):
    if len(capitals[i]) < 5:
        capitals.remove(capitals[i])
print(capitals)