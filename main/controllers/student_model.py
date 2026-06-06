# Student Information System - Model
# Kim Benedick Lauron

students = []

def get_all_students():
    return students

def add_student_to_list(student):
    students.append(student)

def update_student_in_list(index, updated_student):
    students[index] = updated_student

def delete_student_from_list(student):
    students.remove(student)

def get_student_count():
    return len(students)