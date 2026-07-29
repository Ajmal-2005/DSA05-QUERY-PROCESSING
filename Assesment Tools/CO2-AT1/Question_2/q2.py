"""
Question 2 - Library Management Database
A library system to maintain book information using SQLite.
"""

import sqlite3
import os

def main():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'library.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("Connected to SQLite database successfully.")

    # Create Book table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Book (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    print("Book table created successfully.")

    # Clear existing data
    cursor.execute("DELETE FROM Book")
    conn.commit()

    # Insert sample records
    books = [
        (1, 'Introduction to Algorithms', 'Thomas H. Cormen', 'MIT Press', 850.00),
        (2, 'Database System Concepts', 'Abraham Silberschatz', 'McGraw Hill', 720.00),
        (3, 'Python Programming', 'Mark Lutz', 'O Reilly Media', 550.00),
        (4, 'Data Structures Using C', 'Reema Thareja', 'Oxford Press', 450.00),
        (5, 'Operating System Concepts', 'Galvin', 'Wiley', 680.00)
    ]

    cursor.executemany('''
        INSERT INTO Book (book_id, title, author, publisher, price)
        VALUES (?, ?, ?, ?, ?)
    ''', books)
    conn.commit()
    print(f"{len(books)} book records inserted successfully.\n")

    # Display all records before update
    print("Records BEFORE price update:")
    print("=" * 90)
    print(f"{'ID':<6}{'Title':<35}{'Author':<25}{'Publisher':<18}{'Price'}")
    print("=" * 90)

    cursor.execute("SELECT * FROM Book")
    for row in cursor.fetchall():
        print(f"{row[0]:<6}{row[1]:<35}{row[2]:<25}{row[3]:<18}{row[4]:.2f}")
    print("=" * 90)

    # Update the price of a selected book
    update_id = 3
    new_price = 625.00
    cursor.execute("UPDATE Book SET price = ? WHERE book_id = ?", (new_price, update_id))
    conn.commit()
    print(f"\nPrice of Book ID {update_id} updated to {new_price:.2f}")

    # Display updated records
    print("\nRecords AFTER price update:")
    print("=" * 90)
    print(f"{'ID':<6}{'Title':<35}{'Author':<25}{'Publisher':<18}{'Price'}")
    print("=" * 90)

    cursor.execute("SELECT * FROM Book")
    for row in cursor.fetchall():
        print(f"{row[0]:<6}{row[1]:<35}{row[2]:<25}{row[3]:<18}{row[4]:.2f}")
    print("=" * 90)

    conn.close()
    print("\nDatabase connection closed.")

if __name__ == '__main__':
    main()
