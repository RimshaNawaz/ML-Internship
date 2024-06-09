'Contact Management System'
def add_contact(contacts):

    """
    Add a new contact to the contact list.

    Parameters
    ----------
    contacts : dict
        The dictionary storing contact information.

    Returns
    -------
    None
    """
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email address: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")


def view_contacts(contacts):
    """
    View all contacts in the contact list.

    Parameters
    ----------
    contacts : dict
        The dictionary storing contact information.

    Returns
    -------
    None
    """
    if not contacts:
        print("No contacts to display.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"  Phone: {details['phone']}")
            print(f"  Email: {details['email']}")
            print()


def update_contact(contacts):
    """
    Update an existing contact's details.

    Parameters
    ----------
    contacts : dict
        The dictionary storing contact information.

    Returns
    -------
    None
    """
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number for {name} (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address for {name} (current: {contacts[name]['email']}): ")
        contacts[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")


def delete_contact(contacts):
    """
    Delete a contact from the contact list.

    Parameters
    ----------
    contacts : dict
        The dictionary storing contact information.

    Returns
    -------
    None
    """
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")


def main():
    """
    Main function to run the Contact Management System.

    Returns
    -------
    None
    """
    contacts = {}
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
