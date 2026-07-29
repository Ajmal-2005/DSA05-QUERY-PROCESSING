"""
Question 5 - Online Course Registration System
An online learning platform to manage students and course registrations.
Uses SQL JOIN to display student-course relationships.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'course_registration.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create Student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    # Create Course_Registration table with foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course_Registration (
            reg_id INTEGER PRIMARY KEY,
            student_id INTEGER NOT NULL,
            course_name TEXT NOT NULL,
            registration_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Student(student_id)
        )
    ''')
    conn.commit()
    print("Student and Course_Registration tables created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Course_Registration")
    cursor.execute("DELETE FROM Student")
    conn.commit()

    # Insert student records
    students = [
        (401, 'Amit Joshi', 'amit@learn.com', '9001234567'),
        (402, 'Neha Kapoor', 'neha@learn.com', '9001234568'),
        (403, 'Rajesh Iyer', 'rajesh@learn.com', '9001234569'),
        (404, 'Divya Menon', 'divya@learn.com', '9001234570'),
        (405, 'Sunil Patil', 'sunil@learn.com', '9001234571')
    ]

    cursor.executemany('''
        INSERT INTO Student (student_id, name, email, phone)
        VALUES (?, ?, ?, ?)
    ''', students)

    # Insert course registration records
    registrations = [
        (1, 401, 'Python Programming', '2025-02-01'),
        (2, 401, 'Data Science', '2025-02-05'),
        (3, 402, 'Web Development', '2025-02-03'),
        (4, 403, 'Machine Learning', '2025-02-07'),
        (5, 404, 'Python Programming', '2025-02-10'),
        (6, 405, 'Database Management', '2025-02-12')
    ]

    cursor.executemany('''
        INSERT INTO Course_Registration (reg_id, student_id, course_name, registration_date)
        VALUES (?, ?, ?, ?)
    ''', registrations)
    conn.commit()
    print(f"{len(students)} student records inserted.")
    print(f"{len(registrations)} course registration records inserted.\n")

    # Display using SQL JOIN
    print("Student Course Registrations (SQL JOIN):")
    print("=" * 80)
    print(f"{'Reg ID':<10}{'Student Name':<20}{'Email':<25}{'Course':<22}{'Date'}")
    print("=" * 80)

    cursor.execute('''
        SELECT cr.reg_id, s.name, s.email, cr.course_name, cr.registration_date
        FROM Course_Registration cr
        INNER JOIN Student s ON cr.student_id = s.student_id
    ''')

    for row in cursor.fetchall():
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<25}{row[3]:<22}{row[4]}")
    print("=" * 80)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
