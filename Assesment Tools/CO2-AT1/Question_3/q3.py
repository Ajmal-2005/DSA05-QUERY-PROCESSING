"""
Question 3 - Employee and Department Database Design
A company system to store employee and department details using SQLite.
Uses SQL JOIN to display employee-department relationships.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'company.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create Department table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Department (
            dept_id INTEGER PRIMARY KEY,
            dept_name TEXT NOT NULL UNIQUE,
            location TEXT NOT NULL
        )
    ''')

    # Create Employee table with foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            emp_id INTEGER PRIMARY KEY,
            emp_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            salary REAL NOT NULL,
            dept_id INTEGER NOT NULL,
            FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
        )
    ''')
    conn.commit()
    print("Department and Employee tables created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Employee")
    cursor.execute("DELETE FROM Department")
    conn.commit()

    # Insert department records
    departments = [
        (1, 'Computer Science', 'Block A'),
        (2, 'Electronics', 'Block B'),
        (3, 'Mechanical', 'Block C'),
        (4, 'Civil', 'Block D')
    ]

    cursor.executemany('''
        INSERT INTO Department (dept_id, dept_name, location)
        VALUES (?, ?, ?)
    ''', departments)

    # Insert employee records
    employees = [
        (201, 'Ravi Kumar', 30, 55000.00, 1),
        (202, 'Anitha Raj', 28, 48000.00, 2),
        (203, 'Suresh Babu', 35, 62000.00, 3),
        (204, 'Deepa Nair', 26, 45000.00, 1),
        (205, 'Karthik Raman', 32, 58000.00, 4)
    ]

    cursor.executemany('''
        INSERT INTO Employee (emp_id, emp_name, age, salary, dept_id)
        VALUES (?, ?, ?, ?, ?)
    ''', employees)
    conn.commit()
    print(f"{len(departments)} department records inserted.")
    print(f"{len(employees)} employee records inserted.\n")

    # Display using SQL JOIN
    print("Employee Details with Department Names (SQL JOIN):")
    print("=" * 75)
    print(f"{'Emp ID':<10}{'Employee Name':<20}{'Age':<6}{'Salary':<12}{'Department':<20}{'Location'}")
    print("=" * 75)

    cursor.execute('''
        SELECT e.emp_id, e.emp_name, e.age, e.salary, d.dept_name, d.location
        FROM Employee e
        INNER JOIN Department d ON e.dept_id = d.dept_id
    ''')

    for row in cursor.fetchall():
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<6}{row[3]:<12.2f}{row[4]:<20}{row[5]}")
    print("=" * 75)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
