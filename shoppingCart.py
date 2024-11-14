class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def calculate_total_price(self):
        total_price = self.quantity * self.price
        if self.price > 500:
            total_price *= 0.9  
        return total_price


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.shipping_fee = 50
        self.total_cost = 0

    def add_item(self, name, quantity, price):
        item = Item(name, quantity, price)
        self.items.append(item)

    def calculate_total_cost(self):
        item_total = sum(item.calculate_total_price() for item in self.items)
        self.total_cost = item_total + self.shipping_fee
        return self.total_cost

    def save_cart_to_file(self):
        with open("shopping_cart.txt", "a") as file:
            file.write("Shopping Cart Summary:\n")
            for item in self.items:
                file.write(f"Item: {item.name}, Quantity: {item.quantity}, Price per item: Rs.{item.price}\n")
            file.write(f"Total Cost (including shipping): Rs.{self.total_cost}\n")
            file.write("---------------------------------------------------\n")

cart = ShoppingCart()
while True:
    name = input("Enter the name of the item (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    quantity = int(input("Enter the quantity of the item: "))
    price = float(input("Enter the price of the item: "))

    cart.add_item(name, quantity, price)

total_cost = cart.calculate_total_cost()
cart.save_cart_to_file()

print(f"The total cost of your shopping cart is: Rs.{total_cost}")


  
