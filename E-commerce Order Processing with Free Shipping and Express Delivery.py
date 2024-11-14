class Order:
    def __init__(self, weight, order_value, express_delivery=False):
        self.weight = weight
        self.order_value = order_value
        self.express_delivery = express_delivery
        self.shipping_cost = -1  

    def validate_inputs(self):
        return self.weight > 0 and self.order_value >= 0

    def calculate_shipping_cost(self):
        if not self.validate_inputs():
            self.shipping_cost = -1
            return self.shipping_cost

        if self.weight <= 1:
            self.shipping_cost = 50
        elif self.weight <= 5:
            self.shipping_cost = 50 + (self.weight - 1) * 30
        else:
            self.shipping_cost = 50 + (4 * 30) + (self.weight - 5) * 20

        if self.order_value > 2000:
            self.shipping_cost = 0

        if self.express_delivery and self.shipping_cost != 0:
            self.shipping_cost += 100

        return self.shipping_cost

    def save_order_to_file(self):
        try:
            with open("order_details.txt", "a") as file:
                if self.shipping_cost == -1:
                    file.write("Invalid order details. Shipping cost could not be calculated.\n")
                else:
                    file.write(f"Order Value: Rs.{self.order_value}, Weight: {self.weight} kg, "
                               f"Express Delivery: {self.express_delivery}, Shipping Cost: Rs.{self.shipping_cost}\n")
                file.write("---------------------------------------------------\n")
            print("Order details saved successfully.")
        except Exception as e:
            print(f"Error saving order details: {e}")


try:
    weight = float(input("Enter the weight of the package in kg: ").strip())
    order_value = float(input("Enter the total order value in Rs: ").strip())
    express_delivery_input = input("Do you want express delivery? (yes/no): ").strip().lower()
    express_delivery = express_delivery_input == 'yes'

    order = Order(weight, order_value, express_delivery)
    shipping_cost = order.calculate_shipping_cost()

    if shipping_cost == -1:
        print("Invalid order details. Shipping cost could not be calculated.")
    else:
        print(f"The total shipping cost is: Rs.{shipping_cost}")

    order.save_order_to_file()

except ValueError:
    print("Invalid input. Please enter numeric values where required.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
