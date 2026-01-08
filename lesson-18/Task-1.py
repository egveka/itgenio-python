from random import randint

def get_random_array(n=10, stop=100):
    array = []
    for i in range(n):
        array.append(randint(1, stop))
    return array

print(get_random_array())
print(get_random_array(5))
print(get_random_array(3, 10))