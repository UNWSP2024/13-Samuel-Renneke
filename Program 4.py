# Program 4
# Samuel Renneke, 5/1/2026

import sqlite3

DB_NAME = "phonebook.db"

# Create the database
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Entries (
            name TEXT PRIMARY KEY,
            phone TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Create the function for adding entries
def add_entry(name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added successfully.")
    except sqlite3.IntegrityError:
        print("Error: That name already exists.")

    conn.close()

# Create the function for looking up entries
def lookup_entry(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        print(f"{name}'s phone number is: {result[0]}")
    else:
        print("Entry not found.")

    conn.close()

# Create the function for updating entries
def update_entry(name, new_phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("UPDATE Entries SET phone = ? WHERE name = ?", (new_phone, name))

    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("Phone number updated.")

    conn.close()

# Create the function for deleting entries
def delete_entry(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Entries WHERE name = ?", (name,))

    if cursor.rowcount == 0:
        print("Entry not found.")
    else:
        conn.commit()
        print("Entry deleted.")

    conn.close()

# Create the menu function, which lets you choose the option you want
def menu():
    while True:
        print("\nPhonebook Menu")
        print("1. Add Entry")
        print("2. Lookup Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_entry(name, phone)

        elif choice == "2":
            name = input("Enter name to look up: ")
            lookup_entry(name)

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            update_entry(name, phone)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_entry(name)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")

# Run the functions
if __name__ == "__main__":
    create_database()
    menu()
