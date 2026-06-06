# Student Information System - Controller
# Kim Benedick Lauron

from student_model import *
from student_view import *


def add_student():
    show_add_form()
    new_student = get_student_input()

    for student in get_all_students():
        if student[0].lower() == new_student[0].lower():
            show_error("Student ID already exists!")
            return

    add_student_to_list(new_student)
    show_success("Student added successfully!")


def view_all_students():
    students = get_all_students()
    show_student_list(students)


def search_student():
    show_search_form()
    name = get_search_name()

    students = get_all_students()
    found_students = []

    for student in students:
        if name.lower() in student[1].lower():
            found_students.append(student)

    if found_students:
        print(f"\nFound {len(found_students)} student(s):")
        for student in found_students:
            show_student_details(student)
        print()
    else:
        show_student_not_found()


def update_student():
    show_update_form()
    name = get_search_name()

    students = get_all_students()
    found_index = -1

    for i, student in enumerate(students):
        if student[1].lower() == name.lower():
            found_index = i
            break

    if found_index == -1:
        show_student_not_found()
        return

    print("\nCurrent Student Information:")
    show_student_details(students[found_index])

    choice = get_update_choice()

    current_student = students[found_index]
    updated_student = current_student.copy()

    if choice == '1':
        new_id = get_updated_field("Student ID")
        updated_student[0] = new_id
        update_student_in_list(found_index, updated_student)
        show_success("Student ID updated successfully!")

    elif choice == '2':
        new_name = get_updated_field("Name")
        updated_student[1] = new_name
        update_student_in_list(found_index, updated_student)
        show_success("Student name updated successfully!")

    elif choice == '3':
        new_birth = get_updated_field("Birth Date (DD/MM/YYYY)")
        updated_student[2] = new_birth
        update_student_in_list(found_index, updated_student)
        show_success("Birth date updated successfully!")

    elif choice == '4':
        new_course = get_updated_field("Course")
        updated_student[3] = new_course
        update_student_in_list(found_index, updated_student)
        show_success("Course updated successfully!")

    elif choice == '5':
        print("\n--- Enter Updated Information ---")
        new_id = input("Enter new Student ID: ")
        new_name = input("Enter new Student Name: ")
        new_birth = input("Enter new Birth Date (DD/MM/YYYY): ")
        new_course = input("Enter new Course: ")
        updated_student = [new_id, new_name, new_birth, new_course]
        update_student_in_list(found_index, updated_student)
        show_success("All student information updated successfully!")

    else:
        show_error("Invalid choice! No changes made.")


def delete_student():
    show_delete_form()
    name = get_search_name()

    students = get_all_students()

    for student in students:
        if student[1].lower() == name.lower():
            delete_student_from_list(student)
            show_success("Student deleted successfully!")
            return

    show_student_not_found()


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        # Input validation
        if not choice.isdigit():
            show_error("Please enter a number!")
            continue

        choice = int(choice)

        if choice == 1:
            add_student()
        elif choice == 2:
            view_all_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            show_message("\nExiting program... Goodbye!")
            break
        else:
            show_error("Invalid choice! Please enter 1-6.")


if __name__ == "__main__":
    main()