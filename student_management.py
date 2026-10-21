
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


# NEW FEATURE 1: Student Marks
def add_marks():
    roll_number = input("Enter student roll number: ")

    for student in students:
        if student["roll_number"] == roll_number:
            try:
                marks = float(input("Enter student marks (out of 100): "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.\n")
                    return

                student["marks"] = marks
                print("Student marks added successfully!\n")
            except ValueError:
                print("Please enter valid numeric marks.\n")
            return

    print("Student not found. Please check the roll number.\n")


def view_marks():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\n--- Student Marks ---")
    found = False

    for student in students:
        if "marks" in student:
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Marks:", student["marks"], "/ 100")
            print("--------------------")
            found = True

    if not found:
        print("No marks have been added yet.")

    print()


# NEW FEATURE 2: Student Attendance
def mark_attendance():
    roll_number = input("Enter student roll number: ")

    for student in students:
        if student["roll_number"] == roll_number:
            status = input("Enter attendance (Present/Absent): ").strip().lower()

            if status == "present":
                student["attendance"] = "Present"
            elif status == "absent":
                student["attendance"] = "Absent"
            else:
                print("Invalid status. Enter Present or Absent.\n")
                return

            print("Attendance marked successfully!\n")
            return

    print("Student not found. Please check the roll number.\n")


def view_attendance():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\n--- Student Attendance ---")
    found = False

    for student in students:
        if "attendance" in student:
            print("Name:", student["name"])
            print("Roll Number:", student["roll_number"])
            print("Attendance:", student["attendance"])
            print("--------------------")
            found = True

    if not found:
        print("No attendance has been marked yet.")

    print()


def main():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        print("4. Add Student Marks")
        print("5. View Student Marks")
        print("6. Mark Student Attendance")
        print("7. View Student Attendance")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        elif choice == "4":
            add_marks()
        elif choice == "5":
            view_marks()
        elif choice == "6":
            mark_attendance()
        elif choice == "7":
            view_attendance()
        else:
            print("Invalid choice. Please try again.\n")


main()
