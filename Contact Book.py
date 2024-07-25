class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [c for c in self.contacts if search_term.lower() in c.name.lower() or search_term in c.phone]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts found.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    manager = ContactManager()

    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)
        
        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            manager.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the contact manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
