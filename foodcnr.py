class FoodOrder:
    def __init__(self, food_type, quantity, distance):
        self.food_type = food_type.upper()
        self.quantity = quantity
        self.distance = distance
        self.veg_price = 120
        self.non_veg_price = 150
        self.bill_amount = -1

    def validate_data(self):
        if self.food_type not in ['V', 'N']:
            return False
        if self.quantity < 1:
            return False
        if self.distance <= 0:
            return False
        return True

    def calculate_delivery_charge(self):
        if self.distance <= 3:
            return 0
        elif self.distance <= 6:
            return (self.distance - 3) * 3
        else:
            return (6 - 3) * 3 + (self.distance - 6) * 6

    def calculate_total_bill(self):
        if not self.validate_data():
            self.bill_amount = -1
        else:
            if self.food_type == 'V':
                self.bill_amount = self.quantity * self.veg_price
            elif self.food_type == 'N':
                self.bill_amount = self.quantity * self.non_veg_price

            self.bill_amount += self.calculate_delivery_charge()

        return self.bill_amount

    def save_order_to_file(self):
        with open("order_log.txt", "a") as file:
            if self.bill_amount == -1:
                file.write("Invalid order details provided.\n")
            else:
                file.write(f"Order details - Type: {self.food_type}, Quantity: {self.quantity}, Distance: {self.distance} km, Bill Amount: Rs.{self.bill_amount}\n")


food_type = input("Enter type of food (V for Vegetarian, N for Non-Vegetarian): ").strip()
quantity = int(input("Enter quantity of plates: ").strip())
distance = int(input("Enter distance in kms: ").strip())

order = FoodOrder(food_type, quantity, distance)
bill_amount = order.calculate_total_bill()
order.save_order_to_file()

if bill_amount == -1:
    print("Invalid order details provided.")
else:
    print(f"The final bill amount is: Rs.{bill_amount}")
