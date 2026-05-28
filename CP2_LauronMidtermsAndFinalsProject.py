# Student Information System
# Kim Benedick Lauron

students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")

    while True:
        age = input("Enter age: ") 
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid input! Age must be a number.")

    course = input("Enter course: ")

    student = [name, age, course]
    students.append(student)

    print("Student added successfully!\n")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0: 
        print("No students found.\n")
        return

    i = 1
    for student in students:
        print(f"{i}. Name: {student[0]}, Age: {student[1]}, Course: {student[2]}")
        i += 1
    print()


def search_student():
    print("\n--- Search Student ---")

    name = input("Enter name to search: ")

    found = False
    for student in students:
        if student[0].lower() == name.lower():
            print(f"Found: Name: {student[0]}, Age: {student[1]}, Course: {student[2]}")
            found = True

    if not found:
        print("Student not found.")
    print()


def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter name to delete: ")

    for student in students:
        if student[0].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("===== Student Information System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input! Please enter a number.\n")
            continue

        choice = int(choice)

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


menu()