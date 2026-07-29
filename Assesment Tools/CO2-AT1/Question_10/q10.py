"""
Question 10 - Hospital Appointment Management System
A hospital system to manage doctors and appointments using SQLite.
Uses SQL JOIN to display doctor-appointment relationships.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hospital_appointments.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON")

    # Create Doctor table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INTEGER PRIMARY KEY,
            doctor_name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            phone TEXT NOT NULL,
            experience_years INTEGER NOT NULL
        )
    ''')

    # Create Appointment table with foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Appointment (
            appointment_id INTEGER PRIMARY KEY,
            patient_name TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            doctor_id INTEGER NOT NULL,
            FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
        )
    ''')
    conn.commit()
    print("Doctor and Appointment tables created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Appointment")
    cursor.execute("DELETE FROM Doctor")
    conn.commit()

    # Insert doctor records
    doctors = [
        (801, 'Dr. Ramesh Babu', 'Cardiology', '9223344556', 15),
        (802, 'Dr. Anitha Menon', 'Neurology', '9223344557', 10),
        (803, 'Dr. Suresh Reddy', 'Orthopedics', '9223344558', 12),
        (804, 'Dr. Kavitha Iyer', 'Dermatology', '9223344559', 8)
    ]

    cursor.executemany('''
        INSERT INTO Doctor (doctor_id, doctor_name, specialization, phone, experience_years)
        VALUES (?, ?, ?, ?, ?)
    ''', doctors)

    # Insert appointment records
    appointments = [
        (1, 'Rajesh Kumar', '2025-03-10', '09:00 AM', 801),
        (2, 'Priya Das', '2025-03-10', '10:30 AM', 802),
        (3, 'Anil Sharma', '2025-03-11', '11:00 AM', 801),
        (4, 'Deepa Nair', '2025-03-11', '02:00 PM', 803),
        (5, 'Vikram Rao', '2025-03-12', '09:30 AM', 804),
        (6, 'Sunitha Patel', '2025-03-12', '03:00 PM', 802)
    ]

    cursor.executemany('''
        INSERT INTO Appointment (appointment_id, patient_name, appointment_date, appointment_time, doctor_id)
        VALUES (?, ?, ?, ?, ?)
    ''', appointments)
    conn.commit()
    print(f"{len(doctors)} doctor records inserted.")
    print(f"{len(appointments)} appointment records inserted.\n")

    # Display using SQL JOIN
    print("Doctor Appointment Details (SQL JOIN):")
    print("=" * 95)
    print(f"{'Appt ID':<10}{'Patient Name':<18}{'Date':<15}{'Time':<12}{'Doctor Name':<22}{'Specialization'}")
    print("=" * 95)

    cursor.execute('''
        SELECT a.appointment_id, a.patient_name, a.appointment_date, a.appointment_time,
               d.doctor_name, d.specialization
        FROM Appointment a
        INNER JOIN Doctor d ON a.doctor_id = d.doctor_id
    ''')

    for row in cursor.fetchall():
        print(f"{row[0]:<10}{row[1]:<18}{row[2]:<15}{row[3]:<12}{row[4]:<22}{row[5]}")
    print("=" * 95)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
