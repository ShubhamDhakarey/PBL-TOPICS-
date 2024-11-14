import json

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}


class Restaurant:
    def __init__(self):
        self.menu = []
        self.order = []
        self.load_menu()

    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)
        print(f"Added {name} to the menu at Rs.{price}.")

    def view_menu(self):
        if not self.menu:
            print("Menu is empty.")
        else:
            print("Menu:")
            for item in self.menu:
                print(f"{item.name}: Rs.{item.price}")

    def place_order(self, item_name, quantity):
        for item in self.menu:
            if item.name.lower() == item_name.lower():
                self.order.append({"name": item.name, "price": item.price, "quantity": quantity})
                print(f"Added {quantity} x {item.name} to order.")
                return
        print("Item not found in menu.")

    def generate_bill(self):
        total = sum(item["price"] * item["quantity"] for item in self.order)
        print("Order Summary:")
        for item in self.order:
            print(f"{item['name']} x {item['quantity']} = Rs.{item['price'] * item['quantity']}")
        print(f"Total Bill Amount: Rs.{total}")
        return total

    def save_menu(self):
        try:
            with open("menu.json", "w") as file:
                json.dump([item.to_dict() for item in self.menu], file)
            print("Menu saved successfully.")
        except Exception as e:
            print(f"Error saving menu: {e}")

    def load_menu(self):
        try:
            with open("menu.json", "r") as file:
                menu_data = json.load(file)
                self.menu = [MenuItem(item["name"], item["price"]) for item in menu_data]
            print("Menu loaded successfully.")
        except FileNotFoundError:
            print("Menu file not found. Starting with an empty menu.")
        except Exception as e:
            print(f"Error loading menu: {e}")

    def save_order(self):
        try:
            with open("order.json", "w") as file:
                json.dump(self.order, file)
            print("Order saved successfully.")
        except Exception as e:
            print(f"Error saving order: {e}")

    def load_order(self):
        try:
            with open("order.json", "r") as file:
                self.order = json.load(file)
            print("Order loaded successfully.")
        except FileNotFoundError:
            print("Order file not found.")
        except Exception as e:
            print(f"Error loading order: {e}")


# Sample usage
restaurant = Restaurant()

while True:
    print("\nRestaurant Billing Management System")
    print("1. Add new menu item")
    print("2. View menu")
    print("3. Place an order")
    print("4. Generate bill")
    print("5. Save menu and order")
    print("6. Load menu and order")
    print("7. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == '1':
            name = input("Enter the name of the menu item: ")
            price = float(input("Enter the price of the menu item: "))
            restaurant.add_menu_item(name, price)
        elif choice == '2':
            restaurant.view_menu()
        elif choice == '3':
            item_name = input("Enter the name of the item to order: ")
            quantity = int(input("Enter the quantity: "))
            restaurant.place_order(item_name, quantity)
        elif choice == '4':
            restaurant.generate_bill()
        elif choice == '5':
            restaurant.save_menu()
            restaurant.save_order()
        elif choice == '6':
            restaurant.load_menu()
            restaurant.load_order()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
