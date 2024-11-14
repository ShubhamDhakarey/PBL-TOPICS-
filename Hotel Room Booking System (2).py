from datetime import datetime

# Room class to store room information and track availability
class Room:
    def __init__(self, room_type, rate, total_rooms):
        self.room_type = room_type
        self.rate = rate
        self.available_rooms = total_rooms

    def book_room(self, quantity):
        if self.available_rooms >= quantity:
            self.available_rooms -= quantity
            return True
        return False

    def is_available(self, quantity=1):
        return self.available_rooms >= quantity

# Hotel class with rooms and cancellation policies
class Hotel:
    def __init__(self):
        self.rooms = {
            "Standard Room": Room("Standard Room", 3000, 5),  # Example with 5 available rooms
            "Deluxe Room": Room("Deluxe Room", 5000, 3),      # Example with 3 available rooms
            "Suite": Room("Suite", 10000, 2)                  # Example with 2 available rooms
        }
        self.cancellation_policies = {
            "Standard Room": (7, 3),  # (full refund days, partial refund days)
            "Deluxe Room": (10, 5),
            "Suite": (14, 7)
        }

    def get_room(self, room_type):
        return self.rooms.get(room_type)

    def display_available_rooms(self):
        print("\nAvailable Rooms:")
        for room_type, room in self.rooms.items():
            print(f"{room_type}: {room.available_rooms} available")

# Booking class to manage cost calculations
class Booking:
    def __init__(self, room, nights, room_service, quantity):
        self.room = room
        self.nights = nights
        self.room_service = room_service
        self.quantity = quantity
        self.base_cost = room.rate * nights * quantity
        self.room_service_cost = self.base_cost * 0.10 if room_service else 0
        self.discount = self.base_cost * 0.15 if nights > 7 else 0
        self.total_cost = self.base_cost + self.room_service_cost - self.discount

    def display_cost_breakdown(self):
        print(f"Base cost ({self.quantity} rooms for {self.nights} nights): Rs. {self.base_cost}")
        if self.room_service:
            print(f"Room service charge (10%): Rs. {self.room_service_cost}")
        if self.nights > 7:
            print(f"Long stay discount (15%): -Rs. {self.discount}")
        print(f"Total cost: Rs. {self.total_cost}")

# Function to calculate refund based on the policy
def calculate_refund(booking, hotel, cancellation_date, check_in_date):
    days_before_check_in = (check_in_date - cancellation_date).days
    full_refund_days, partial_refund_days = hotel.cancellation_policies[booking.room.room_type]
    
    if days_before_check_in > full_refund_days:
        refund = booking.total_cost
    elif days_before_check_in > partial_refund_days:
        refund = booking.total_cost * 0.5
    else:
        refund = 0
    print(f"Refund amount: Rs. {refund}")
    return refund

# Function to parse date
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# Main function
def main():
    hotel = Hotel()

    while True:
        # Display available rooms at the start
        hotel.display_available_rooms()

        room_type = input("\nEnter room type (Standard Room, Deluxe Room, Suite): ")
        room = hotel.get_room(room_type)

        if not room:
            print("Invalid room type.")
            continue

        try:
            quantity = int(input("Enter the number of rooms to book: "))
            if quantity <= 0:
                print("Invalid number of rooms.")
                continue
        except ValueError:
            print("Invalid input for number of rooms.")
            continue

        if not room.is_available(quantity):
            print(f"Sorry, only {room.available_rooms} {room_type}(s) are available.")
            available_rooms = [rtype for rtype, r in hotel.rooms.items() if r.is_available()]
            if available_rooms:
                print("Available room types:", ", ".join(available_rooms))
            else:
                print("No rooms available.")
            continue

        try:
            nights = int(input("Enter number of nights: "))
            if nights <= 0:
                print("Invalid number of nights.")
                continue
        except ValueError:
            print("Invalid input for nights.")
            continue

        room_service = input("Do you need room service? (yes/no): ").strip().lower() == "yes"
        check_in_date = parse_date(input("Enter check-in date (YYYY-MM-DD): "))
        if not check_in_date:
            print("Invalid check-in date.")
            continue

        # Book room(s) and create booking
        if room.book_room(quantity):
            booking = Booking(room, nights, room_service, quantity)
            booking.display_cost_breakdown()
            print(f"\nRoom(s) booked! Total cost: Rs. {booking.total_cost:.2f}")

            # Handle cancellation
            if input("Do you want to cancel the booking? (yes/no): ").strip().lower() == "yes":
                cancellation_date = parse_date(input("Enter cancellation date (YYYY-MM-DD): "))
                if cancellation_date:
                    calculate_refund(booking, hotel, cancellation_date, check_in_date)
                else:
                    print("Invalid cancellation date.")
        else:
            print(f"Sorry, {room_type} is now fully booked.")
            continue

        # Exit or book another room
        if input("\nDo you want to make another booking? (yes/no): ").strip().lower() != "yes":
            break

# Run the program
if __name__ == "__main__":
    main()
