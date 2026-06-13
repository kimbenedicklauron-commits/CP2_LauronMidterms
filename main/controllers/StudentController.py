# Student Information System - Controller

from StudentModel import *
from StudentView import *


def add_student():
    show_add_form()

    student_id = input("Enter Student ID (5-6 digits): ")

    if not validate_student_id(student_id):
        show_error("Student ID must be 5-6 digits long!")
        return

    if check_student_id_exists(student_id):
        show_error("Student ID already exists!")
        return

    name = input("Enter Student Name (First and Last): ")

    if not validate_name(name):
        show_error("Name must include both first and last name!")
        return

    birth_date = input("Enter Birth Date (DD/MM/YYYY): ")
    course = input("Enter Course: ")

    new_student = [student_id, name, birth_date, course]

    if add_student_to_list(new_student):
        show_success("Student added successfully!")
    else:
        show_error("Failed to add student!")


def search_student():
    if get_student_count() == 0:
        show_no_students()
        return

    show_search_form()
    choice = get_search_choice()

    if choice == '1':
        name = get_search_name()
        students = search_student_by_name(name)

        if students:
            show_student_list(students)
        else:
            show_student_not_found()

    elif choice == '2':
        student_id = get_search_id()
        student = find_student_by_id(student_id)

        if student:
            print("\n--- Student Found ---")
            show_student_details(student)
            print()
        else:
            show_student_not_found()

    else:
        show_error("Invalid choice!")


def update_student():
    if get_student_count() == 0:
        show_no_students()
        return

    show_update_form()

    print("\nSearch student to update:")
    search_choice = get_search_choice()

    found_student = None
    original_id = None

    if search_choice == '1':
        name = get_search_name()
        found_student = find_student_by_name(name)
        if found_student:
            original_id = found_student[0]

    elif search_choice == '2':
        student_id = get_search_id()
        found_student = find_student_by_id(student_id)
        if found_student:
            original_id = found_student[0]

    else:
        show_error("Invalid choice!")
        return

    if not found_student:
        show_student_not_found()
        return

    print("\nCurrent Student Information:")
    show_student_details(found_student)

    option = get_update_option()

    updated_student = found_student.copy()

    if option == '1':
        field_choice = get_update_choice()

        if field_choice == '1':
            new_id = get_updated_field("Student ID")

            if not validate_student_id(new_id):
                show_error("Student ID must be 5-6 digits long!")
                return

            if new_id != original_id and check_student_id_exists(new_id):
                show_error("Student ID already belongs to another student!")
                return

            updated_student[0] = new_id

        elif field_choice == '2':
            new_name = get_updated_field("Name")

            if not validate_name(new_name):
                show_error("Name must include both first and last name!")
                return

            updated_student[1] = new_name

        elif field_choice == '3':
            new_birth = get_updated_field("Birth Date (DD/MM/YYYY)")
            updated_student[2] = new_birth

        elif field_choice == '4':
            new_course = get_updated_field("Course")
            updated_student[3] = new_course

        else:
            show_error("Invalid choice! No changes made.")
            return

        update_student_by_index(original_id, updated_student)
        show_success("Student information updated successfully!")

    elif option == '2':
        print("\n--- Enter Updated Information (leave blank to keep current) ---")

        # Update ID
        new_id = input(f"Enter new Student ID (current: {updated_student[0]}): ")
        if new_id:
            if not validate_student_id(new_id):
                show_error("Student ID must be 5-6 digits long!")
                return

            if new_id != original_id and check_student_id_exists(new_id):
                show_error("Student ID already belongs to another student!")
                return

            updated_student[0] = new_id

        new_name = input(f"Enter new Name (current: {updated_student[1]}): ")
        if new_name:
            if not validate_name(new_name):
                show_error("Name must include both first and last name!")
                return

            updated_student[1] = new_name

        new_birth = input(f"Enter new Birth Date (current: {updated_student[2]}): ")
        if new_birth:
            updated_student[2] = new_birth

        new_course = input(f"Enter new Course (current: {updated_student[3]}): ")
        if new_course:
            updated_student[3] = new_course

        update_student_by_index(original_id, updated_student)
        show_success("Student information updated successfully!")

    elif option == '3':
        print("\n--- Enter Updated Information ---")

        new_id = input("Enter new Student ID: ")
        if not validate_student_id(new_id):
            show_error("Student ID must be 5-6 digits long!")
            return

        if new_id != original_id and check_student_id_exists(new_id):
            show_error("Student ID already belongs to another student!")
            return

        new_name = input("Enter new Student Name: ")
        if not validate_name(new_name):
            show_error("Name must include both first and last name!")
            return

        new_birth = input("Enter new Birth Date (DD/MM/YYYY): ")
        new_course = input("Enter new Course: ")

        updated_student = [new_id, new_name, new_birth, new_course]
        update_student_by_index(original_id, updated_student)
        show_success("All student information updated successfully!")

    else:
        show_error("Invalid choice! No changes made.")


def delete_student():
    if get_student_count() == 0:
        show_no_students()
        return

    show_delete_form()

    choice = get_delete_choice()

    if choice == '1':  # Delete by name
        name = get_search_name()

        print(f"\nAre you sure you want to delete student '{name}'?")
        confirm = input("Type 'YES' to confirm: ")

        if confirm == 'YES':
            if delete_student_from_list(name, 'name'):
                show_success("Student deleted successfully!")
            else:
                show_student_not_found()
        else:
            show_message("Deletion cancelled.\n")

    elif choice == '2':
        student_id = get_search_id()

        # Confirm deletion
        print(f"\nAre you sure you want to delete student with ID '{student_id}'?")
        confirm = input("Type 'YES' to confirm: ")

        if confirm == 'YES':
            if delete_student_from_list(student_id, 'id'):
                show_success("Student deleted successfully!")
            else:
                show_student_not_found()
        else:
            show_message("Deletion cancelled.\n")

    else:
        show_error("Invalid choice!")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if not choice.isdigit():
            show_error("Please enter a number!")
            continue

        choice = int(choice)

        if choice == 1:
            add_student()
        elif choice == 2:
            search_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            show_message("\nExiting program... Goodbye!")
            break
        else:
            show_error("Invalid choice! Please enter 1-5.")