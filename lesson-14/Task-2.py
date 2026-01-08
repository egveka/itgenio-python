numbers = [int(i) for i in input().split()]
num_sort_reverse = sorted(numbers, reverse=True)

if numbers == num_sort_reverse:
    print("YES")
else:
    print("NO")