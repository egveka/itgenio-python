def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

print((2*factorial(5) + 3*factorial(8)) / (factorial(6) + factorial(4)))

print(factorial(15))