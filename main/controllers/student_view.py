# Student Information System - View
# Kim Benedick Lauron

def show_menu():
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def show_add_form():
    print("\n--- Add New Student ---")


def show_update_form():
    print("\n--- Update Student Information ---")


def show_search_form():
    print("\n--- Search Student ---")


def show_delete_form():
    print("\n--- Delete Student ---")


def show_student_list(students):
    print("\n--- Complete Student List ---")

    if len(students) == 0:
        print("No students found.\n")
        return

    print(f"Total Students: {len(students)}")
    print("-" * 50)
    for i, student in enumerate(students, 1):
        print(f"{i}. ID: {student[0]}, Name: {student[1]}, Birth Date: {student[2]}, Course: {student[3]}")
    print("-" * 50)
    print()


def show_student_details(student):
    print(f"ID: {student[0]}, Name: {student[1]}, Birth Date: {student[2]}, Course: {student[3]}")


def show_message(message):
    print(message)


def get_student_input():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    birth_date = input("Enter Birth Date (DD/MM/YYYY): ")
    course = input("Enter Course: ")
    return [student_id, name, birth_date, course]


def get_search_name():
    return input("Enter name to search: ")


def get_update_choice():
    print("\nWhat would you like to update?")
    print("1. Student ID")
    print("2. Name")
    print("3. Birth Date")
    print("4. Course")
    print("5. Update All Information")
    return input("Enter your choice: ")


def get_updated_field(field_name):
    return input(f"Enter new {field_name}: ")


def show_no_students():
    print("No students found in the system.\n")


def show_student_not_found():
    print("Student not found.\n")


def show_success(message):
    print(f"✓ {message}\n")


def show_error(message):
    print(f"✗ {message}\n")