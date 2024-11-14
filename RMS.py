def calculate_total(cart, shipping_fee):
    total = 0
    for item in cart:
        name, quantity, price = item
        if price > 500:
            price = price * 0.90  # Apply 10% discount
        total += quantity * price
    total += shipping_fee
    return total

# Input from the user
cart = []
shipping_fee = 50
while True:
    name = input("Enter the item name (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    quantity = int(input(f"Enter the quantity for {name}: "))
    price = float(input(f"Enter the price for {name}: "))
    cart.append((name, quantity, price))

# Calculate total
total_cost = calculate_total(cart, shipping_fee)
print(f"Total cost of the shopping cart is: Rs. {total_cost:.2f}")
