"""
Question 9 - Vehicle Registration Database
A transport department system to maintain vehicle registration details using SQLite.
Supports search by registration number.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vehicle.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Vehicle table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vehicle (
            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reg_number TEXT UNIQUE NOT NULL,
            owner_name TEXT NOT NULL,
            vehicle_type TEXT NOT NULL,
            brand TEXT NOT NULL,
            model_year INTEGER NOT NULL,
            fuel_type TEXT NOT NULL CHECK(fuel_type IN ('Petrol', 'Diesel', 'Electric', 'CNG'))
        )
    ''')
    conn.commit()
    print("Vehicle table created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Vehicle")
    conn.commit()

    # Insert vehicle records
    vehicles = [
        ('TN01AB1234', 'Kiran Raj', 'Car', 'Hyundai', 2022, 'Petrol'),
        ('KA02CD5678', 'Meera Sharma', 'Bike', 'Honda', 2023, 'Petrol'),
        ('MH03EF9012', 'Vivek Gupta', 'Car', 'Tata', 2021, 'Diesel'),
        ('DL04GH3456', 'Aarti Singh', 'SUV', 'Mahindra', 2023, 'Diesel'),
        ('AP05IJ7890', 'Naveen Kumar', 'Car', 'MG', 2024, 'Electric')
    ]

    cursor.executemany('''
        INSERT INTO Vehicle (reg_number, owner_name, vehicle_type, brand, model_year, fuel_type)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', vehicles)
    conn.commit()
    print(f"{len(vehicles)} vehicle records inserted.\n")

    # Display all records
    print("All Vehicle Records:")
    print("=" * 90)
    print(f"{'ID':<6}{'Reg Number':<15}{'Owner':<18}{'Type':<8}{'Brand':<12}{'Year':<8}{'Fuel'}")
    print("=" * 90)

    cursor.execute("SELECT * FROM Vehicle")
    for row in cursor.fetchall():
        print(f"{row[0]:<6}{row[1]:<15}{row[2]:<18}{row[3]:<8}{row[4]:<12}{row[5]:<8}{row[6]}")
    print("=" * 90)

    # Search for a vehicle by registration number
    search_reg = 'MH03EF9012'
    print(f"\nSearching for vehicle with Registration Number: {search_reg}")
    print("-" * 60)

    cursor.execute("SELECT * FROM Vehicle WHERE reg_number = ?", (search_reg,))
    result = cursor.fetchone()

    if result:
        print(f"  Vehicle ID     : {result[0]}")
        print(f"  Reg Number     : {result[1]}")
        print(f"  Owner Name     : {result[2]}")
        print(f"  Vehicle Type   : {result[3]}")
        print(f"  Brand          : {result[4]}")
        print(f"  Model Year     : {result[5]}")
        print(f"  Fuel Type      : {result[6]}")
    else:
        print("  Vehicle not found.")
    print("-" * 60)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
