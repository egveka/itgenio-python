from random import randint

def get_random_array(n=10):
    seq = []
    for i in range(n):
        seq.append(randint(1, 100))
    return seq

def reverse(seq):
    new_seq = []
    for i in range(len(seq)):
        new_seq.append(seq[-i-1])
    return new_seq

array = get_random_array(5)
print(array)
print(reverse(array))