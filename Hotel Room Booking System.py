class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.status = "available"

    def book_room(self):
        if self.status == "available":
            self.status = "booked"
            return True
        return False

    def check_in(self):
        if self.status == "booked":
            self.status = "occupied"
            return True
        return False

    def check_out(self):
        if self.status == "occupied":
            self.status = "available"
            return True
        return False


class Hotel:
    def __init__(self, num_rooms):
        self.rooms = [Room(room_number=i+1) for i in range(num_rooms)]

    def display_status(self):
        print("Current Room Status:")
        for room in self.rooms:
            print(f"Room {room.room_number}: {room.status}")

    def book_room(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            room = self.rooms[room_number - 1]
            if room.book_room():
                print(f"Room {room_number} has been booked successfully.")
            else:
                print(f"Room {room_number} is not available for booking.")
        else:
            print("Invalid room number.")

    def check_in(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            room = self.rooms[room_number - 1]
            if room.check_in():
                print(f"Check-in successful for Room {room_number}.")
            else:
                print(f"Room {room_number} is not booked yet.")
        else:
            print("Invalid room number.")

    def check_out(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            room = self.rooms[room_number - 1]
            if room.check_out():
                print(f"Check-out successful for Room {room_number}.")
            else:
                print(f"Room {room_number} is not currently occupied.")
        else:
            print("Invalid room number.")

    def save_status_to_file(self):
        with open("room_status.txt", "w") as file:
            file.write("Room Status:\n")
            for room in self.rooms:
                file.write(f"Room {room.room_number}: {room.status}\n")

hotel = Hotel(num_rooms=10)

while True:
    print("\nHotel Room Booking System")
    print("1. Display room status")
    print("2. Book a room")
    print("3. Check-in to a room")
    print("4. Check-out of a room")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hotel.display_status()
    elif choice == 2:
        room_number = int(input("Enter room number to book: "))
        hotel.book_room(room_number)
    elif choice == 3:
        room_number = int(input("Enter room number to check in: "))
        hotel.check_in(room_number)
    elif choice == 4:
        room_number = int(input("Enter room number to check out: "))
        hotel.check_out(room_number)
    elif choice == 5:
        hotel.save_status_to_file()
        print("Status saved to file. Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")

        
