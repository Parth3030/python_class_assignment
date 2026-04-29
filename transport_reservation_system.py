import random

class BusReservation:
    def __init__(self):
        # 1. Route Configuration: { Route_Name: Price }
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 800,
            "Ahmedabad to Udaipur": 750
        }
        
        # 2. Seat Tracking: { Route_Name: [List of Booked Seat Numbers] }
        self.seat_inventory = {route: [] for route in self.routes}
        
        # 3. Ticket Database: { TicketID: {details} }
        self.tickets = {}

    def show_routes(self):
        print("\n--- Available Routes ---")
        for i, (route, price) in enumerate(self.routes.items(), 1):
            available_seats = 40 - len(self.seat_inventory[route])
            print(f"{i}. {route} - ₹{price} ({available_seats} seats left)")

    def book_ticket(self):
        self.show_routes()
        route_list = list(self.routes.keys())
        
        try:
            choice = int(input("\nSelect Route Number: ")) - 1
            if not (0 <= choice < len(route_list)):
                print("Invalid Route.")
                return
            
            selected_route = route_list[choice]
            
            # Check if bus is full
            if len(self.seat_inventory[selected_route]) >= 40:
                print("Sorry, this bus is fully booked!")
                return

            # Passenger Details
            name = input("Passenger Name: ").strip().title()
            age = int(input("Age: "))
            mobile = input("Mobile Number (10 digits): ").strip()
            
            if len(mobile) != 10 or not mobile.isdigit():
                print("Invalid Mobile Number.")
                return

            # Assign Seat (Finding the first empty number 1-40)
            booked_seats = self.seat_inventory[selected_route]
            seat_no = next(s for s in range(1, 41) if s not in booked_seats)

            # Generate Ticket ID
            ticket_id = f"TIC{random.randint(10000, 99999)}"
            
            # Save Booking
            self.tickets[ticket_id] = {
                "name": name,
                "route": selected_route,
                "seat": seat_no,
                "price": self.routes[selected_route]
            }
            self.seat_inventory[selected_route].append(seat_no)
            
            print(f"\nBooking Confirmed!")
            print(f"Ticket ID: {ticket_id} | Seat: {seat_no} | Fare: ₹{self.routes[selected_route]}")

        except (ValueError, StopIteration):
            print("Invalid input or No seats available.")

    def view_ticket(self):
        tid = input("\nEnter Ticket ID: ").strip().upper()
        if tid in self.tickets:
            t = self.tickets[tid]
            print(f"\n--- Ticket Details [{tid}] ---")
            print(f"Passenger: {t['name']} | Route: {t['route']}")
            print(f"Seat No: {t['seat']} | Status: Confirmed")
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        tid = input("\nEnter Ticket ID to cancel: ").strip().upper()
        if tid in self.tickets:
            ticket_info = self.tickets[tid]
            # Release the seat
            self.seat_inventory[ticket_info['route']].remove(ticket_info['seat'])
            # Delete record
            del self.tickets[tid]
            print(f"Ticket {tid} has been cancelled. Refund processed.")
        else:
            print("Ticket not found.")

    def run(self):
        while True:
            print("\n=== Bus Reservation System ===")
            print("1. Show Routes\n2. Book Ticket\n3. View Ticket\n4. Cancel Ticket\n5. Exit")
            cmd = input("Select: ")
            if cmd == '1': self.show_routes()
            elif cmd == '2': self.book_ticket()
            elif cmd == '3': self.view_ticket()
            elif cmd == '4': self.cancel_ticket()
            elif cmd == '5': break
            else: print("Invalid Choice.")

if __name__ == "__main__":
    bus_system = BusReservation()
    bus_system.run()
