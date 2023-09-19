# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            print()

def search_contact():
    query = input("Enter name or phone number to search for a contact: ")
    found = False
    for name, contact_info in contacts.items():
        if query in name or query == contact_info['Phone']:
            print(f"Name: {name}")
            print(f"Phone: {contact_info['Phone']}")
            print(f"Email: {contact_info['Email']}")
            print(f"Address: {contact_info['Address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contacts:
        print(f"Current Contact Information for {name}:")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        choice = input("What do you want to update (phone/email/address): ").lower()
        if choice in ['phone', 'email', 'address']:
            new_info = input(f"Enter the new {choice}: ")
            contacts[name][choice.capitalize()] = new_info
            print(f"{choice.capitalize()} updated successfully!")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
