# Student Information System
# Kim Benedick Lauron

students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")

    while not name.strip():
        print("Error: Name cannot be empty!")
        name = input("Enter student name: ")

    while True:
        age = input("Enter age: ")
        if age.isdigit():
            age = int(age)
            if 1 <= age <= 120:
                break
            else:
                print("Invalid input! Age must be between 1 and 120.")
        else:
            print("Invalid input! Age must be a number.")

    course = input("Enter course: ")

    while not course.strip():
        print("Error: Course cannot be empty!")
        course = input("Enter course: ")

    student = [name, age, course]
    students.append(student)

    print("Student added successfully!\n")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.\n")
        return

    print(f"{'No.':<4} {'Name':<20} {'Age':<6} {'Course':<20}")
    print("-" * 50)
    i = 1
    for student in students:
        print(f"{i:<4} {student[0]:<20} {student[1]:<6} {student[2]:<20}")
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


def update_student():
    print("\n--- Update Student Information ---")

    if len(students) == 0:
        print("No students available to update.\n")
        return

    name = input("Enter the name of the student to update: ")

    for i, student in enumerate(students):
        if student[0].lower() == name.lower():
            print(f"\nCurrent information for {student[0]}:")
            print(f"1. Name: {student[0]}")
            print(f"2. Age: {student[1]}")
            print(f"3. Course: {student[2]}")

            print("\nWhat would you like to update?")
            print("1. Name")
            print("2. Age")
            print("3. Course")
            print("4. Update All")
            print("5. Cancel")

            choice = input("Enter your choice: ")

            if not choice.isdigit():
                print("Invalid input! Please enter a number.\n")
                return

            choice = int(choice)

            if choice == 1:
                new_name = input("Enter new name: ")
                while not new_name.strip():
                    print("Error: Name cannot be empty!")
                    new_name = input("Enter new name: ")
                students[i][0] = new_name
                print("Student name updated successfully!\n")

            elif choice == 2:
                while True:
                    new_age = input("Enter new age: ")
                    if new_age.isdigit():
                        new_age = int(new_age)
                        if 1 <= new_age <= 120:
                            students[i][1] = new_age
                            print("Student age updated successfully!\n")
                            break
                        else:
                            print("Invalid input! Age must be between 1 and 120.")
                    else:
                        print("Invalid input! Age must be a number.")

            elif choice == 3:
                new_course = input("Enter new course: ")
                while not new_course.strip():
                    print("Error: Course cannot be empty!")
                    new_course = input("Enter new course: ")
                students[i][2] = new_course
                print("Student course updated successfully!\n")

            elif choice == 4:
                print("\n--- Updating all information ---")

                new_name = input(f"Enter new name (current: {students[i][0]}): ")
                if new_name.strip():
                    students[i][0] = new_name

                while True:
                    new_age = input(f"Enter new age (current: {students[i][1]}): ")
                    if not new_age:
                        break
                    elif new_age.isdigit():
                        new_age = int(new_age)
                        if 1 <= new_age <= 120:
                            students[i][1] = new_age
                            break
                        else:
                            print("Age must be between 1 and 120. Update cancelled for age.")
                            break
                    else:
                        print("Invalid input! Age must be a number. Update cancelled for age.")
                        break

                new_course = input(f"Enter new course (current: {students[i][2]}): ")
                if new_course.strip():
                    students[i][2] = new_course

                print("Student information updated successfully!\n")

            elif choice == 5:
                print("Update cancelled.\n")

            else:
                print("Invalid choice! Update cancelled.\n")

            return

    print("Student not found.\n")


def delete_student():
    print("\n--- Delete Student ---")

    name = input("Enter name to delete: ")

    for student in students:
        if student[0].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete {student[0]}? (y/n): ")
            if confirm.lower() == 'y':
                students.remove(student)
                print("Student deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("===== Student Information System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

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
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    menu()