numbers = {1, 2, 2, 2, 3, 3, 4, 4, 5, 6}
even_numbers = {number for number in numbers if number % 2 == 0}
print(*even_numbers)

print()

numbers2 = {1, 2, 3}
numbers2.update(i ** 2 for i in [1, 2, 3])
print(numbers2)

print()

prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
fibonnaci = {0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
prime_fibonnaci = prime.intersection(fibonnaci)
print(*prime_fibonnaci)
print(*prime & fibonnaci)

print()

fruits = {"apple", "orange"}
fruits2 = {"orange", "banana", "pear"}
all_fruits = fruits | fruits2
all_fruits2 = fruits.union(fruits2)
print(*all_fruits)
print(*all_fruits2)

print()

# i_know = {"Python", "Go", "Java"}
# you_know = {"Scratch", "C#", "C++", "Java"}
# you_know_but_i_dont = you_know - i_know
# print(*you_know_but_i_dont)
i_know = {"Python", "Go", "Java"}
you_know = {"Scratch":1 , "C#":2, "C++":3, "Java":4}
i_know_but_you_dont = i_know.difference(you_know)
print(*i_know_but_you_dont)

print()

non_positive = {-3, -2, -1, 0}
non_negative = {0, 1, 2, 3}
non_zero = non_positive ^ non_negative
print(*non_zero)