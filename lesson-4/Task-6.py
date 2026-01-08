price = 0
all_items_cost = 0

while price >= 0:
    if price > 1500:
        price = price - price * 8 / 100
    all_items_cost += price
    price = float(input("Cost: "))
print("Checkout: ", all_items_cost, "$")