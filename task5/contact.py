contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Search by name or phone: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    search_name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            print("Leave blank to keep current value.")
            contact['phone'] = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            contact['email'] = input(f"New email [{contact['email']}]: ") or contact['email']
            contact['address'] = input(f"New address [{contact['address']}]: ") or contact['address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    search_name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
