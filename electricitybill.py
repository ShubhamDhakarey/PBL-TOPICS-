class ElectricityBill:
    def __init__(self, usage):
        self.usage = usage
        self.bill_amount = -1

    def validate_usage(self):
        return self.usage > 0

    def calculate_bill(self):
        if not self.validate_usage():
            self.bill_amount = -1
            return self.bill_amount

        if self.usage <= 100:
            self.bill_amount = self.usage * 5
        elif self.usage <= 200:
            self.bill_amount = (100 * 5) + ((self.usage - 100) * 7)
        else:
            self.bill_amount = (100 * 5) + (100 * 7) + ((self.usage - 200) * 10)

        if self.usage > 250:
            self.bill_amount *= 1.1  
        elif self.usage < 50:
            self.bill_amount -= 100 

        return self.bill_amount

    def save_bill_to_file(self):
        with open("electricity_bill.txt", "a") as file:
            if self.bill_amount == -1:
                file.write("Invalid usage provided. Bill amount could not be calculated.\n")
            else:
                file.write(f"Monthly Usage: {self.usage} units, Bill Amount: Rs.{self.bill_amount}\n")
            file.write("---------------------------------------------------\n")


usage = int(input("Enter monthly electricity usage in units: ").strip())
bill = ElectricityBill(usage)
bill_amount = bill.calculate_bill()
bill.save_bill_to_file()

if bill_amount == -1:
    print("Invalid usage provided. Bill amount could not be calculated.")
else:
    print(f"The total bill amount is: Rs.{bill_amount}")
