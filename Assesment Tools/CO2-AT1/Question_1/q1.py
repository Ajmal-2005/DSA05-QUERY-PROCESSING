"""
Question 1 - Student Database Design and Connectivity
A college automation system for managing student records using SQLite.
"""

import sqlite3
import os

def main():
    # Database file path
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'student.db')

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Student table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    print("Student table created successfully.")

    # Clear existing data for clean execution
    cursor.execute("DELETE FROM Student")
    conn.commit()

    # Insert at least five student records
    students = [
        (101, 'Arun Kumar', 20, 'Male', 'Computer Science', 'arun@college.edu'),
        (102, 'Priya Sharma', 21, 'Female', 'Electronics', 'priya@college.edu'),
        (103, 'Rahul Verma', 19, 'Male', 'Mechanical', 'rahul@college.edu'),
        (104, 'Sneha Patel', 22, 'Female', 'Civil', 'sneha@college.edu'),
        (105, 'Vikram Singh', 20, 'Male', 'Computer Science', 'vikram@college.edu')
    ]

    cursor.executemany('''
        INSERT INTO Student (student_id, name, age, gender, department, email)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', students)
    conn.commit()
    print(f"{len(students)} student records inserted successfully.\n")

    # Display all records
    print("=" * 80)
    print(f"{'ID':<8}{'Name':<20}{'Age':<6}{'Gender':<10}{'Department':<20}{'Email'}")
    print("=" * 80)

    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]:<8}{row[1]:<20}{row[2]:<6}{row[3]:<10}{row[4]:<20}{row[5]}")

    print("=" * 80)
    print(f"\nTotal records: {len(rows)}")

    # Close connection
    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
