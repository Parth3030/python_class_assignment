class SchoolManagement:
    def __init__(self):
        # Database: { 'STU1001': {'name': 'Rahul', 'age': 10, ...} }
        self.students = {}
        self.id_counter = 1001  

    def add_student(self):
        print("\n--- New Admission ---")
        name = input("Enter Student Name: ").strip().title()
        
        
        try:
            age = int(input("Enter Age (5-18): "))
            if not (5 <= age <= 18):
                print("Admission Denied: Age must be between 5 and 18.")
                return
        except ValueError:
            print("Invalid input: Age must be a number.")
            return

        # 2. Class Validation
        try:
            student_class = int(input("Enter Class (1-12): "))
            if not (1 <= student_class <= 12):
                print("Invalid Class: Must be between 1 and 12.")
                return
        except ValueError:
            print("Invalid input: Class must be a number.")
            return

        # 3. Mobile Validation
        mobile = input("Enter Guardian Mobile (10 digits): ").strip()
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Invalid Mobile: Must be exactly 10 digits.")
            return

        # 4. Generate ID and Save
        student_id = f"STU{self.id_counter}"
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }
        print(f"Admission Successful! Assigned ID: {student_id}")
        self.id_counter += 1 # Increment for the next student

    def view_student(self):
        sid = input("\nEnter Student ID (e.g., STU1001): ").strip().upper()
        if sid in self.students:
            s = self.students[sid]
            print(f"\n--- Student Details [{sid}] ---")
            print(f"Name: {s['name']} | Age: {s['age']} | Class: {s['class']} | Mobile: {s['mobile']}")
        else:
            print("Record not found.")

    def update_student(self):
        sid = input("\nEnter Student ID to update: ").strip().upper()
        if sid not in self.students:
            print("Record not found.")
            return

        print("1. Update Mobile | 2. Update Class")
        choice = input("Select option: ")
        
        if choice == '1':
            new_mobile = input("Enter new 10-digit mobile: ").strip()
            if new_mobile.isdigit() and len(new_mobile) == 10:
                self.students[sid]['mobile'] = new_mobile
                print("Mobile updated.")
            else:
                print("Invalid mobile format.")
        elif choice == '2':
            new_class = input("Enter new class (1-12): ")
            if new_class.isdigit() and 1 <= int(new_class) <= 12:
                self.students[sid]['class'] = int(new_class)
                print("Class updated.")
            else:
                print("Invalid class.")

    def remove_student(self):
        sid = input("\nEnter Student ID to remove: ").strip().upper()
        if sid in self.students:
            confirm = input(f"Are you sure you want to delete {self.students[sid]['name']}? (y/n): ")
            if confirm.lower() == 'y':
                del self.students[sid]
                print(f"Record {sid} deleted.")
        else:
            print("Record not found.")

    def run(self):
        while True:
            print("\n=== School Management System ===")
            print("1. New Admission\n2. View Details\n3. Update Record\n4. Remove Record\n5. Exit")
            choice = input("Select an option: ")
            if choice == '1': self.add_student()
            elif choice == '2': self.view_student()
            elif choice == '3': self.update_student()
            elif choice == '4': self.remove_student()
            elif choice == '5': break
            else: print("Invalid choice.")

if __name__ == "__main__":
    school = SchoolManagement()
    school.run()
