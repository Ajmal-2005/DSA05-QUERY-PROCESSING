"""
Question 7 - Inventory Management System
A retail store system to maintain product inventory using SQLite.
Identifies low-stock products and updates their quantities.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inventory.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Product table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Product (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK(quantity >= 0),
            unit_price REAL NOT NULL CHECK(unit_price > 0)
        )
    ''')
    conn.commit()
    print("Product table created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Product")
    conn.commit()

    # Insert sample products
    products = [
        (601, 'Laptop', 'Electronics', 25, 45000.00),
        (602, 'Mouse', 'Electronics', 8, 500.00),
        (603, 'Notebook', 'Stationery', 5, 50.00),
        (604, 'Pen Drive', 'Electronics', 3, 350.00),
        (605, 'Desk Chair', 'Furniture', 15, 8000.00),
        (606, 'Marker Set', 'Stationery', 7, 120.00),
        (607, 'Monitor', 'Electronics', 12, 15000.00)
    ]

    cursor.executemany('''
        INSERT INTO Product (product_id, product_name, category, quantity, unit_price)
        VALUES (?, ?, ?, ?, ?)
    ''', products)
    conn.commit()
    print(f"{len(products)} product records inserted.\n")

    # Display all products
    print("All Products:")
    print("=" * 70)
    print(f"{'ID':<8}{'Product Name':<18}{'Category':<15}{'Quantity':<12}{'Unit Price'}")
    print("=" * 70)

    cursor.execute("SELECT * FROM Product")
    for row in cursor.fetchall():
        print(f"{row[0]:<8}{row[1]:<18}{row[2]:<15}{row[3]:<12}{row[4]:.2f}")
    print("=" * 70)

    # Identify products with quantity less than 10
    print("\nProducts with Quantity < 10 (Low Stock):")
    print("-" * 70)

    cursor.execute("SELECT * FROM Product WHERE quantity < 10")
    low_stock = cursor.fetchall()
    for row in low_stock:
        print(f"  {row[0]:<8}{row[1]:<18}{row[2]:<15}{row[3]:<12}{row[4]:.2f}")
    print(f"\nTotal low-stock products: {len(low_stock)}")

    # Update stock quantity of low-stock products (restock by adding 20)
    restock_amount = 20
    cursor.execute("UPDATE Product SET quantity = quantity + ? WHERE quantity < 10", (restock_amount,))
    conn.commit()
    print(f"\nRestocked all low-stock products by adding {restock_amount} units.")

    # Display updated inventory
    print("\nUpdated Inventory:")
    print("=" * 70)
    print(f"{'ID':<8}{'Product Name':<18}{'Category':<15}{'Quantity':<12}{'Unit Price'}")
    print("=" * 70)

    cursor.execute("SELECT * FROM Product")
    for row in cursor.fetchall():
        print(f"{row[0]:<8}{row[1]:<18}{row[2]:<15}{row[3]:<12}{row[4]:.2f}")
    print("=" * 70)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
