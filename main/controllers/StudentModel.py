# Student Information System - Model

import sqlite3


def get_db_connection():
    conn = sqlite3.connect('students.db')
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            course TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT student_id, name, birth_date, course FROM students ORDER BY name")
    students = cursor.fetchall()

    conn.close()
    return [list(student) for student in students]


def add_student_to_list(student):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO students (student_id, name, birth_date, course)
            VALUES (?, ?, ?, ?)
        ''', (student[0], student[1], student[2], student[3]))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def update_student_by_index(student_id, updated_student):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE students 
        SET student_id = ?, name = ?, birth_date = ?, course = ?
        WHERE student_id = ?
    ''', (updated_student[0], updated_student[1], updated_student[2], updated_student[3], student_id))

    conn.commit()
    conn.close()


def delete_student_from_list(identifier, search_by='name'):
    conn = get_db_connection()
    cursor = conn.cursor()

    if search_by == 'name':
        cursor.execute("DELETE FROM students WHERE name = ?", (identifier,))
    else:
        cursor.execute("DELETE FROM students WHERE student_id = ?", (identifier,))

    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()

    return deleted_count > 0


def search_student_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT student_id, name, birth_date, course 
        FROM students 
        WHERE name LIKE ?
        ORDER BY name
    ''', (f'%{name}%',))

    students = cursor.fetchall()
    conn.close()
    return [list(student) for student in students]


def check_student_id_exists(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT student_id FROM students WHERE student_id = ?", (student_id,))
    exists = cursor.fetchone() is not None

    conn.close()
    return exists


def find_student_by_name(name):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT student_id, name, birth_date, course FROM students WHERE name = ?", (name,))
    student = cursor.fetchone()

    conn.close()
    return list(student) if student else None


def find_student_by_id(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT student_id, name, birth_date, course FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()

    conn.close()
    return list(student) if student else None


def get_student_count():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    count = cursor.fetchone()[0]

    conn.close()
    return count


create_table()