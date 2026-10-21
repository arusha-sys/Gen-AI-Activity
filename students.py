
import json
import os

DATA_FILE = "students.json"
SUBJECTS = ["English", "Mathematics", "Computer Science"]
students = []


def load_students():
    global students

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                students = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load records. Starting with an empty list.")
            students = []


def save_students():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def find_student(roll_number):
    for student in students:
        if student["roll_number"] == roll_number:
            return student
    return None


def get_marks():
    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks


def get_attendance():
    while True:
        try:
            attended = int(input("Classes attended: "))
            total = int(input("Total classes held: "))

            if total <= 0:
                print("Total classes must be greater than zero.")
            elif attended < 0 or attended > total:
                print("Attendance must be between 0 and total classes.")
            else:
                return {
                    "attended": attended,
                    "total": total
                }

        except ValueError:
            print("Please enter whole numbers.")


def add_student():
    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    if find_student(roll_number):
        print("This roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    print("\nEnter subject-wise marks:")
    marks = get_marks()

    print("\nEnter attendance:")
    attendance = get_attendance()

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "attendance": attendance
    }

    students.append(student)
    save_students()
    print("Student added and saved successfully!")


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def show_report(student):
    marks = student["marks"]
    total_marks = sum(marks.values())
    maximum_marks = len(marks) * 100
    percentage = (total_marks / maximum_marks) * 100

    attendance = student["attendance"]
    attendance_percentage = (
        attendance["attended"] / attendance["total"]
    ) * 100

    print("\n--- Student Performance Report ---")
    print("Name:", student["name"])
    print("Roll Number:", student["roll_number"])

    for subject, mark in marks.items():
        print(f"{subject}: {mark}/100")

    print(f"Total Marks: {total_marks:g}/{maximum_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", get_grade(percentage))
    print(f"Attendance: {attendance_percentage:.2f}%")
    print("----------------------------------")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        show_report(student)


def update_student():
    roll_number = input("Enter roll number to update: ").strip()
    student = find_student(roll_number)

    if student is None:
        print("Student not found.")
        return

    new_name = input(
        f"Enter new name (press Enter to keep {student['name']}): "
    ).strip()

    if new_name:
        student["name"] = new_name

    print("\nEnter the updated marks for all subjects:")
    student["marks"] = get_marks()

    print("\nEnter updated attendance:")
    student["attendance"] = get_attendance()

    save_students()
    print("Student information updated successfully!")


def main():
    load_students()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Performance Reports")
        print("3. Update Student")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
