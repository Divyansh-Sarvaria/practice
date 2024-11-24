flights = {}
bookings = []

def cancel_booking(booking_id):
    for booking in bookings:
        if booking['booking_id'] == booking_id:
            bookings.remove(booking)
            flights[booking['flight_id']]['available_seats'] += 1
            print(f"Booking ID {booking_id} has been canceled.")
            return
    print(f"No booking found with ID {booking_id}.")

def view_bookings():
    print("\nYour Bookings:")
    if not bookings:
        print("No bookings found.")
        return
    for booking in bookings:
        flight_id = booking['flight_id']
        flight_details = flights.get(flight_id, {})
        date = flight_details.get('date', 'Unknown')
        print(f"Booking ID: {booking['booking_id']}, Customer: {booking['customer_name']}, "
              f"Flight ID: {flight_id}, Flight Date: {date}")

def book_ticket(customer_name, flight_id):
    if flight_id not in flights:
        print(f"No flight found with ID {flight_id}.")
        return
    flight = flights[flight_id]
    if flight['available_seats'] > 0:
        flight['available_seats'] -= 1
        booking_id = len(bookings) + 1
        bookings.append({
            'booking_id': booking_id,
            'customer_name': customer_name,
            'flight_id': flight_id,
        })
        print(f"Ticket booked successfully! Booking ID: {booking_id}")
    else:
        print("No seats available for this flight.")

def view_flights():
    print("\nAvailable Flights:")
    if not flights:
        print("No flights available.")
        return
    for flight_id, details in flights.items():
        print(f"Flight ID: {flight_id}, "
              f"Date: {details['date']}, Available Seats: {details['available_seats']}")

def add_flight(flight_id, destination, date, seats):

    flights[flight_id] = {
        'destination': destination,
        'date': date,
        'seats': seats,
        'available_seats': seats
    }
    print(f"Flight {flight_id} added successfully!")

def menu():
    while True:
        print("\n--- Flight Booking System ---")
        print("1. Add Flight")
        print("2. View Flights")
        print("3. Book Ticket")
        print("4. View Bookings")
        print("5. Cancel Booking")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            flight_id = input("Enter flight ID: ")
            destination = input("Enter destination: ")
            date = input("Enter date (YYYY-MM-DD): ")
            seats = int(input("Enter number of seats: "))
            add_flight(flight_id, destination, date, seats)
        elif choice == '2':
            view_flights()
        elif choice == '3':
            customer_name = input("Enter customer name: ")
            flight_id = input("Enter flight ID: ")
            book_ticket(customer_name, flight_id)
        elif choice == '4':
            view_bookings()
        elif choice == '5':
            booking_id = int(input("Enter booking ID: "))
            cancel_booking(booking_id)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
