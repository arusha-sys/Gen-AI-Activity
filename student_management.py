
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


def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        print("\n--- Student List ---")
        for student in students:
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("--------------------")
        print()


def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main()
