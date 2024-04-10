import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS contacts
             (name TEXT, number TEXT)''')

def add_contact(name, number):
    c.execute("INSERT INTO contacts (name, number) VALUES (?, ?)", (name, number))
    conn.commit()
    print("Contact added successfully!")

def delete_contact(keyword):
    c.execute("DELETE FROM contacts WHERE name=? OR number=?", (keyword, keyword))
    if c.rowcount > 0:
        conn.commit()
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact(keyword):
    c.execute("SELECT * FROM contacts WHERE name LIKE ? OR number LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    contacts = c.fetchall()
    if contacts:
        print("Search Results:")
        for contact in contacts:
            print("Name:", contact[0])
            print("Number:", contact[1])
    else:
        print("No contacts found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == '2':
            keyword = input("Enter contact name or number to delete: ")
            delete_contact(keyword)
        elif choice == '3':
            keyword = input("Enter name or number to search: ")
            search_contact(keyword)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
