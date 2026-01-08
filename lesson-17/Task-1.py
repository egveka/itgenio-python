def sell(products, price):
    profit = products * price
    print(f"Profit is: {profit}")

products = int(input("How much products do we have: "))
price = int(input("What price are we selling each one for: "))
sell(products, price)