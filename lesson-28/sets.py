correct_empty_set = set()
# print(type(correct_empty_set))

colors = {"red", "green", "green", "blue", "purple", "purple"}
colors = (set(colors))
print(*colors)
print()

word = "hello"
word = set(word)
print(*word)
print()

fruits = {"banana", "apple", "orange", "orange"}
fruits2 = {"apple", "apple", "banana", "orange", "orange"}
print(fruits == fruits2)
print()

colors2 = {"red", "green", "blue", "blue"}
if "green" in colors2:
    print("Yes!")
print(len(colors2))
print()

for color in colors2:
    print(color)
print()

colors2.add("red")
colors2.add("purple")
print(*colors2)
print()

fruits3 = {"apple", "orange", "banana"}
fruits3.discard("banana")
print(*fruits3)