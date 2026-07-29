"""
Question 6 - Banking Account Management System
A bank system to maintain customer account information using SQLite.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'banking.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Account table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            account_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            account_type TEXT NOT NULL CHECK(account_type IN ('Savings', 'Current')),
            balance REAL NOT NULL CHECK(balance >= 0),
            phone TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    conn.commit()
    print("Account table created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Account")
    conn.commit()

    # Insert customer account details
    accounts = [
        (5001, 'Ramesh Kumar', 'Savings', 25000.00, '9112345678', 'Chennai'),
        (5002, 'Sunita Devi', 'Current', 150000.00, '9112345679', 'Mumbai'),
        (5003, 'Ajay Mehta', 'Savings', 45000.00, '9112345680', 'Delhi'),
        (5004, 'Pooja Reddy', 'Savings', 32000.00, '9112345681', 'Hyderabad'),
        (5005, 'Manish Tiwari', 'Current', 200000.00, '9112345682', 'Bangalore')
    ]

    cursor.executemany('''
        INSERT INTO Account (account_id, customer_name, account_type, balance, phone, address)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', accounts)
    conn.commit()
    print(f"{len(accounts)} account records inserted.\n")

    # Display all records before update
    print("All Customer Records (Before Update):")
    print("=" * 85)
    print(f"{'Acc ID':<10}{'Customer Name':<20}{'Type':<12}{'Balance':<14}{'Phone':<14}{'Address'}")
    print("=" * 85)

    cursor.execute("SELECT * FROM Account")
    for row in cursor.fetchall():
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<12}{row[3]:<14.2f}{row[4]:<14}{row[5]}")
    print("=" * 85)

    # Update account balance
    update_id = 5003
    new_balance = 52000.00
    cursor.execute("UPDATE Account SET balance = ? WHERE account_id = ?", (new_balance, update_id))
    conn.commit()
    print(f"\nBalance of Account ID {update_id} updated to {new_balance:.2f}")

    # Display all records after update
    print("\nAll Customer Records (After Update):")
    print("=" * 85)
    print(f"{'Acc ID':<10}{'Customer Name':<20}{'Type':<12}{'Balance':<14}{'Phone':<14}{'Address'}")
    print("=" * 85)

    cursor.execute("SELECT * FROM Account")
    for row in cursor.fetchall():
        print(f"{row[0]:<10}{row[1]:<20}{row[2]:<12}{row[3]:<14.2f}{row[4]:<14}{row[5]}")
    print("=" * 85)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
