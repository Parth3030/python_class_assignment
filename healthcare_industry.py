class ClinicAppointment:
    def __init__(self):
        self.doctors = ["Dr. Sharma", "Dr. Reddy", "Dr. Kapoor"]
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        
        # Structure: { 'Dr. Sharma': {'10am': [pt1, pt2], '11am': [] ...}, ... }
        self.availability = {doc: {slot: [] for slot in self.slots} for doc in self.doctors}
        
        self.appointments = {}

    def book_appointment(self):
        print("\n--- Book Appointment ---")
        name = input("Patient Name: ").strip()
        age = input("Age: ").strip()
        mobile = input("Mobile Number: ").strip()
        
        # Check if patient already has a booking
        if mobile in self.appointments:
            print("Error: An appointment already exists for this mobile number.")
            return

        print("\nAvailable Doctors:", self.doctors)
        doc_choice = input("Enter Doctor Name: ").strip()
        
        if doc_choice not in self.doctors:
            print("Invalid Doctor Name.")
            return

        print(f"Time Slots: {self.slots}")
        slot_choice = input("Preferred Time Slot: ").strip().lower()

        if slot_choice not in self.slots:
            print("Invalid Time Slot.")
            return

        # Check availability (Max 3 patients per slot per doctor)
        current_bookings = self.availability[doc_choice][slot_choice]
        if len(current_bookings) < 3:
            appt_details = {
                "name": name,
                "age": age,
                "doctor": doc_choice,
                "slot": slot_choice
            }
            # Save to both data structures
            current_bookings.append(mobile)
            self.appointments[mobile] = appt_details
            print(f"Confirmed! Appointment with {doc_choice} at {slot_choice} for {name}.")
        else:
            print(f"Sorry, {slot_choice} for {doc_choice} is fully booked.")

    def view_or_cancel(self):
        mobile = input("\nEnter registered mobile number: ").strip()
        if mobile not in self.appointments:
            print("No appointment found for this number.")
            return

        appt = self.appointments[mobile]
        print(f"\n--- Appointment Details ---")
        print(f"Patient: {appt['name']} | Doctor: {appt['doctor']} | Time: {appt['slot']}")
        
        choice = input("Type 'CANCEL' to delete or 'EXIT' to go back: ").upper()
        if choice == 'CANCEL':
            # Remove from availability tracker
            self.availability[appt['doctor']][appt['slot']].remove(mobile)
            # Remove from master records
            del self.appointments[mobile]
            print("🗑️ Appointment cancelled successfully.")

    def run(self):
        while True:
            print("\n=== Clinic Management System ===")
            print("1. Book Appointment")
            print("2. View/Cancel Appointment")
            print("3. Exit")
            choice = input("Select an option: ")
            
            if choice == '1':
                self.book_appointment()
            elif choice == '2':
                self.view_or_cancel()
            elif choice == '3':
                print("Exiting system. Stay healthy!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    clinic = ClinicAppointment()
    clinic.run()
