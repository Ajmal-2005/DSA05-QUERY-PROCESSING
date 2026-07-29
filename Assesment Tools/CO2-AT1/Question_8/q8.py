"""
Question 8 - Course and Faculty Management System
A university system to manage faculty and courses using SQLite.
Uses SQL JOIN to display faculty-course relationships.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'university.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create Faculty table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Faculty (
            faculty_id INTEGER PRIMARY KEY,
            faculty_name TEXT NOT NULL,
            designation TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Create Course table with foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            course_id TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER NOT NULL,
            faculty_id INTEGER NOT NULL,
            FOREIGN KEY (faculty_id) REFERENCES Faculty(faculty_id)
        )
    ''')
    conn.commit()
    print("Faculty and Course tables created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Course")
    cursor.execute("DELETE FROM Faculty")
    conn.commit()

    # Insert faculty records
    faculty = [
        (701, 'Dr. Srinivasan', 'Professor', 'Computer Science', 'srini@univ.edu'),
        (702, 'Dr. Meena Kumari', 'Associate Professor', 'Mathematics', 'meena@univ.edu'),
        (703, 'Dr. Ashok Verma', 'Professor', 'Physics', 'ashok@univ.edu'),
        (704, 'Dr. Priya Nair', 'Assistant Professor', 'Computer Science', 'priya@univ.edu')
    ]

    cursor.executemany('''
        INSERT INTO Faculty (faculty_id, faculty_name, designation, department, email)
        VALUES (?, ?, ?, ?, ?)
    ''', faculty)

    # Insert course records
    courses = [
        ('CS101', 'Data Structures', 4, 701),
        ('CS102', 'Database Systems', 3, 701),
        ('MA201', 'Linear Algebra', 3, 702),
        ('PH301', 'Quantum Physics', 4, 703),
        ('CS103', 'Python Programming', 3, 704),
        ('MA202', 'Probability', 3, 702)
    ]

    cursor.executemany('''
        INSERT INTO Course (course_id, course_name, credits, faculty_id)
        VALUES (?, ?, ?, ?)
    ''', courses)
    conn.commit()
    print(f"{len(faculty)} faculty records inserted.")
    print(f"{len(courses)} course records inserted.\n")

    # Display using SQL JOIN
    print("Faculty and Course Details (SQL JOIN):")
    print("=" * 90)
    print(f"{'Course ID':<12}{'Course Name':<22}{'Credits':<10}{'Faculty Name':<22}{'Designation':<22}{'Dept'}")
    print("=" * 90)

    cursor.execute('''
        SELECT c.course_id, c.course_name, c.credits, f.faculty_name, f.designation, f.department
        FROM Course c
        INNER JOIN Faculty f ON c.faculty_id = f.faculty_id
    ''')

    for row in cursor.fetchall():
        print(f"{row[0]:<12}{row[1]:<22}{row[2]:<10}{row[3]:<22}{row[4]:<22}{row[5]}")
    print("=" * 90)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
