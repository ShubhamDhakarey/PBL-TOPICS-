import datetime

class AirlineTicket:
    def __init__(self, flight_date, booking_date, class_type, luggage_weight, preferred_seat):
        self.flight_date = datetime.datetime.strptime(flight_date, "%Y-%m-%d")
        self.booking_date = datetime.datetime.strptime(booking_date, "%Y-%m-%d")
        self.class_type = class_type
        self.luggage_weight = luggage_weight
        self.preferred_seat = preferred_seat
        self.base_prices = {
            'Economy': 5000,
            'Business': 12000,
            'First': 20000
        }
        self.luggage_fee = 200
    def calculate_ticket_price(self):
        if self.luggage_weight < 0 or self.booking_date > self.flight_date:
            return -1

        base_price = self.base_prices[self.class_type]
        luggage_fee = max(0, self.luggage_weight - 15) * self.luggage_fee
        seat_fee = 500 if self.preferred_seat else 0

        days_in_advance = (self.flight_date - self.booking_date).days
        discount = 0.1 * base_price if days_in_advance >= 60 else 0

        total_price = base_price + luggage_fee + seat_fee - discount
        return total_price

def main():
    print("Airline Ticket Booking System")
    print("1. Book a ticket")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        flight_date = input("Enter flight date (YYYY-MM-DD): ")
        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        class_type = input("Enter class type (Economy/Business/First): ")
        luggage_weight = float(input("Enter luggage weight (kg): "))
        preferred_seat = input("Do you want preferred seat? (yes/no): ")
        preferred_seat = preferred_seat.lower() == 'yes'

        ticket = AirlineTicket(flight_date, booking_date, class_type, luggage_weight, preferred_seat)
        total_price = ticket.calculate_ticket_price()
        if total_price == -1:
            print("Invalid input")
        else:
            print(f"Total ticket price: Rs. {total_price}")

        # Save ticket to file
        with open("tickets.txt", "a") as file:
            file.write(f"{flight_date},{booking_date},{class_type},{luggage_weight},{preferred_seat},{total_price}\n")

    elif choice == '3':
        pass

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


     
