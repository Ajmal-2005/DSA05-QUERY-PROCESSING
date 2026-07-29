"""
Question 4 - Hospital Patient Database
A hospital system to manage patient information using SQLite.
Demonstrates INSERT, UPDATE, DELETE, and SELECT operations.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hospital.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Patient table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient (
            patient_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            disease TEXT NOT NULL,
            contact TEXT NOT NULL,
            admission_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    print("Patient table created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Patient")
    conn.commit()

    # Insert patient records
    patients = [
        (301, 'Mohan Das', 45, 'Male', 'Diabetes', '9876543210', '2025-01-10'),
        (302, 'Lakshmi Devi', 30, 'Female', 'Typhoid', '9876543211', '2025-01-12'),
        (303, 'Arjun Reddy', 55, 'Male', 'Heart Disease', '9876543212', '2025-01-15'),
        (304, 'Kavitha Rao', 28, 'Female', 'Malaria', '9876543213', '2025-01-18'),
        (305, 'Sanjay Gupta', 60, 'Male', 'Asthma', '9876543214', '2025-01-20')
    ]

    cursor.executemany('''
        INSERT INTO Patient (patient_id, name, age, gender, disease, contact, admission_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', patients)
    conn.commit()
    print(f"{len(patients)} patient records inserted.\n")

    # Display all records
    print("All Patient Records:")
    print("=" * 95)
    print(f"{'ID':<8}{'Name':<18}{'Age':<6}{'Gender':<10}{'Disease':<18}{'Contact':<15}{'Admission'}")
    print("=" * 95)

    cursor.execute("SELECT * FROM Patient")
    for row in cursor.fetchall():
        print(f"{row[0]:<8}{row[1]:<18}{row[2]:<6}{row[3]:<10}{row[4]:<18}{row[5]:<15}{row[6]}")
    print("=" * 95)

    # Update contact number of a specified patient
    update_id = 302
    new_contact = '9999988888'
    cursor.execute("UPDATE Patient SET contact = ? WHERE patient_id = ?", (new_contact, update_id))
    conn.commit()
    print(f"\nContact number of Patient ID {update_id} updated to {new_contact}.")

    # Delete a discharged patient's record
    delete_id = 304
    cursor.execute("DELETE FROM Patient WHERE patient_id = ?", (delete_id,))
    conn.commit()
    print(f"Patient ID {delete_id} (discharged) record deleted.")

    # Display remaining records
    print("\nRemaining Patient Records:")
    print("=" * 95)
    print(f"{'ID':<8}{'Name':<18}{'Age':<6}{'Gender':<10}{'Disease':<18}{'Contact':<15}{'Admission'}")
    print("=" * 95)

    cursor.execute("SELECT * FROM Patient")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]:<8}{row[1]:<18}{row[2]:<6}{row[3]:<10}{row[4]:<18}{row[5]:<15}{row[6]}")
    print("=" * 95)
    print(f"\nTotal remaining records: {len(rows)}")

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
