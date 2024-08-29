import re

class ContactMng:
    def __init__(self):
        self.contacts = {}

    def validate_phone_no(self, phone_no):
        return len(phone_no) == 10 and phone_no.isdigit()

    def validate_email(self, email):
        return re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email) is not None

    def add_contact(self, name, phone_no, email, address):
        if not self.validate_phone_no(phone_no):
            print("Invalid phone number. It must be of 10 digits.")
            return
        if not self.validate_email(email):
            print("Invalid Email Id. It must be a valid Gmail Id.")
            return
        self.contacts[name] = {
            'phone_number': phone_no,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for name, details in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)

    def search_contact(self, search_term):
        found = False
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone_number']:
                print(f"Name: {name}")
                print(f"Phone Number: {details['phone_number']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("-" * 20)
                found = True
        if not found:
            print("No contact found.")

    def update_contact(self, name, phone_no=None, email=None, address=None):
        if name in self.contacts:
            if phone_no:
                if not self.validate_phone_no(phone_no):
                    print("Invalid phone number. It must be of 10 digits.")
                    return
                self.contacts[name]['phone_number'] = phone_no
            if email:
                if not self.validate_email(email):
                    print("Invalid email address. It must be a valid Gmail address.")
                    return
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")

def main():
    manager = ContactMng()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_no = input("Enter phone number: ")
            email = input("Enter Gmail address: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone_no, email, address)
        
        elif choice == '2':
            manager.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone_no = input("Enter new phone number (10 digits, leave blank to keep current): ")
            email = input("Enter new email (Gmail address, leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, phone_no if phone_no else None, 
                                   email if email else None, 
                                   address if address else None)
        
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        
        elif choice == '6':
            print("Successfully Exited...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
