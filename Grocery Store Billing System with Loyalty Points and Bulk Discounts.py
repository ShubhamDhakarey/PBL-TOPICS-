import datetime

class GroceryStore:
    def __init__(self):
        self.items = {
            "fruits": {"price": 50, "quantity": 0, "type": "kg"},
            "vegetables": {"price": 30, "quantity": 0, "type": "kg"},
            "dairy": {"price": 80, "quantity": 0, "type": "liter"}
        }
        self.loyalty_points = 0
        self.total_bill = -1

    def add_item_quantity(self, item_name, quantity):
        if item_name in self.items and quantity > 0:
            self.items[item_name]["quantity"] += quantity
            print(f"Added {quantity} {self.items[item_name]['type']} of {item_name}.")
        else:
            print(f"Invalid item or quantity. {item_name} not added.")

    def calculate_bill(self, day_of_week, loyalty_points=0):
        if not self.validate_quantities():
            self.total_bill = -1
            return self.total_bill

        subtotal = 0
        for item, details in self.items.items():
            quantity = details["quantity"]
            price = details["price"]

            item_cost = quantity * price
            if quantity > 10:
                item_cost *= 0.9

            subtotal += item_cost

        if day_of_week in ["Saturday", "Sunday"]:
            subtotal *= 0.95 

        if loyalty_points > 0:
            discount = min(loyalty_points, int(subtotal))
            subtotal -= discount
            self.loyalty_points -= discount 

        self.total_bill = subtotal

        earned_points = int(subtotal // 100)
        self.loyalty_points += earned_points
        print(f"Loyalty points earned: {earned_points}. Total points available: {self.loyalty_points}")

        return self.total_bill

    def validate_quantities(self):
        return all(item["quantity"] > 0 for item in self.items.values())

    def save_bill_to_file(self):
        try:
            with open("grocery_bill.txt", "a") as file:
                if self.total_bill == -1:
                    file.write("Invalid quantities provided. Bill could not be calculated.\n")
                else:
                    file.write(f"Total Bill Amount: Rs.{self.total_bill}\n")
                    file.write(f"Loyalty Points Available: {self.loyalty_points}\n")
                    file.write("---------------------------------------------------\n")
            print("Bill saved successfully.")
        except Exception as e:
            print(f"Error saving bill: {e}")

store = GroceryStore()

try:
    day_of_week = datetime.datetime.today().strftime("%A")
    print(f"Today is {day_of_week}.")

    store.add_item_quantity("fruits", int(input("Enter quantity of fruits (kg): ").strip()))
    store.add_item_quantity("vegetables", int(input("Enter quantity of vegetables (kg): ").strip()))
    store.add_item_quantity("dairy", int(input("Enter quantity of dairy products (liters): ").strip()))

    loyalty_points = int(input("Enter loyalty points to redeem: ").strip())

    total_bill = store.calculate_bill(day_of_week, loyalty_points)
    if total_bill == -1:
        print("Invalid quantities provided. Bill could not be calculated.")
    else:
        print(f"The total bill amount is: Rs.{total_bill}")

    store.save_bill_to_file()

except ValueError:
    print("Invalid input. Please enter positive numeric values for quantities and loyalty points.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
