# Student Information System - View

def show_menu():
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def show_add_form():
    print("\n--- Add New Student ---")

def show_update_form():
    print("\n--- Update Student Information ---")

def show_search_form():
    print("\n--- Search Student ---")

def show_delete_form():
    print("\n--- Delete Student ---")

def show_student_list(students):
    if len(students) == 0:
        print("\nNo students found.\n")
        return

    print(f"\nFound {len(students)} student(s):")
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
    student_id = input("Enter Student ID (5-6 digits): ")
    name = input("Enter Student Name (First and Last): ")
    birth_date = input("Enter Birth Date (DD/MM/YYYY): ")
    course = input("Enter Course: ")
    return [student_id, name, birth_date, course]

def get_search_choice():
    print("\nSearch by:")
    print("1. Name")
    print("2. Student ID")
    return input("Enter your choice: ")

def get_search_name():
    return input("Enter name to search: ")

def get_search_id():
    return input("Enter Student ID to search: ")

def get_update_option():
    print("\nWhat would you like to update?")
    print("1. Update single field")
    print("2. Update multiple fields (but not all)")
    print("3. Update all fields")
    return input("Enter your choice: ")

def get_update_choice():
    print("\nWhich field would you like to update?")
    print("1. Student ID")
    print("2. Name")
    print("3. Birth Date")
    print("4. Course")
    return input("Enter your choice: ")

def get_updated_field(field_name):
    return input(f"Enter new {field_name}: ")

def get_delete_choice():
    print("\nDelete by:")
    print("1. Name")
    print("2. Student ID")
    return input("Enter your choice: ")

def show_no_students():
    print("\n No students registered in the database yet!\n")

def show_student_not_found():
    print("\n Student not found.\n")

def show_success(message):
    print(f"\n {message}\n")

def show_error(message):
    print(f"\n {message}\n")

def validate_student_id(student_id):
    return student_id.isdigit() and 5 <= len(student_id) <= 6

def validate_name(name):
    name_parts = name.strip().split()
    return len(name_parts) >= 2