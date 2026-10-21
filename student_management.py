students = []

def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_number": roll_number
    }

    students.append(student)
    print("Student added successfully!\n")


def search_student():
    roll_number = input("Enter roll number to search: ")
    found = False
    
    for student in students:
        if student["roll_number"] == roll_number:
            print("\n--- Student Found ---")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("---------------------\n")
            found = True
            break
            
    if not found:
        print("Student not found with this roll number.\n")


def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()