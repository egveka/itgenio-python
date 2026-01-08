limit = int(input())
fib1 = 1
fib2 = 1
print(fib1)

while fib2 <= limit:
    print(fib2)
    old_fib2 = fib2
    fib2 += fib1
    fib1 = old_fib2