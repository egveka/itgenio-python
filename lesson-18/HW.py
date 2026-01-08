fruits = ["pineapple", "lemon", "pear", "watermelon", "tomato", "apple"]
first, second, *middle, second_to_last, last = fruits
print(f"First element {first}")
print(f"Second element{second}")
print(f"Middle{middle}")
print(f"Second-to-last {second_to_last}")
print(f"Last{last}")