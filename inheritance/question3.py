# Class 1
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_passenger(self):
        print("Passenger Details:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")

# Class 2
class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

    def display_ticket(self):
        print(f"  Ticket Number: {self.ticket_number}")
        print(f"  Seat Number: {self.seat_number}")

# Combined class 
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def display_booking(self):
        self.display_passenger()
        self.display_ticket()
booking = Booking("Sam", 30, "TKT12", "14B")
booking.display_booking()