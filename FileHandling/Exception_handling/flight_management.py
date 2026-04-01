# Custom Exceptions
class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

# Read flight data from file
flights = {}

try:
    file = open("/home/sanjukta/pythonTraining/FileHandling/Exception_handling/flight.txt", "r")
    for line in file:
        parts = line.strip().split()
        if len(parts) == 3:
            flight_number = parts[0]
            available_seats = int(parts[1])
            price_per_ticket = float(parts[2])
            flights[flight_number] = [available_seats, price_per_ticket]
except FileNotFoundError:
    print("Error: flights.txt file not found.")
finally:
    if file:
        file.close()

# If no flights loaded, stop the program
if not flights:
    print("No flight data available.")
else:
    # Start booking process
    try:
        user_flight = input("Enter flight number: ")

        if user_flight not in flights:
            raise FlightNotFoundError("Flight not found.")

        try:
            num_tickets = int(input("Enter number of tickets to book: "))

            if num_tickets == 0:
                raise ZeroDivisionError("Cannot book 0 tickets.")

            available_seats = flights[user_flight][0]
            price = flights[user_flight][1]

            if num_tickets > available_seats:
                raise SeatsUnavailableError("Not enough seats available.")

            total_cost = num_tickets * price
            discount_per_ticket = total_cost / num_tickets
            print("flight details")

            print("Flight number:", user_flight,)
            print("Available Seats:", available_seats)
            print("Price per Ticket: ₹", price)
            print("Tickets Booked:", num_tickets)
            print("Total Cost: ₹", total_cost)
            print("Discount per Ticket: ₹", round(discount_per_ticket, 2))

        except ValueError:
            print("Invalid input: Enter a valid number for tickets.")
        except ZeroDivisionError as e:
            print("Error:", e)
        except SeatsUnavailableError as e:
            print("Error:", e)

    except FlightNotFoundError as e:
        print("Error:", e)
