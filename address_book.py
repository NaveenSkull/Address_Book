"""

@Author: Naveen Madev Naik
@Date: 2024-09-10
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-09-10
@Title: Ability to add multiple persons, display, edit, and delete contacts in multiple Address Books using OOP

"""

import re
import mylogging

logger = mylogging.logger_init("address_book_system.py")


class Contact:

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def display(self):

        """
        Description:
            Displays the contact details.

        Parameter:
            self:Instance of the class

        Return:
            None
        """

        print("----------------------------------------------------")
        logger.info(f"Name: {self.first_name} {self.last_name}\n"
                    f"Address: {self.address}\n"
                    f"City: {self.city}\n"
                    f"State: {self.state}\n"
                    f"Zip Code: {self.zip_code}\n"
                    f"Phone Number: {self.phone_number}\n"
                    f"Email: {self.email}\n")

    def update_contact(self, **kwargs):

        """
        Description:
            Updates contact details with the provided values.

        Parameter:
            self:Instance of the class
            **kwargs:keyword arguements takes multiple arguement

        Return:
            None
        """

        for key, value in kwargs.items():
            setattr(self, key, value)
        logger.info(f"Contact {self.first_name} {self.last_name} updated successfully.")


class AddressBook:

    def __init__(self, name):
        self.name = name
        self.contacts = []

    @staticmethod
    def get_valid_input(prompt, regex_pattern=None, error_message="Invalid input. Please try again."):

        """
        Description:
            Prompts the user for input and validates it against a regex pattern if provided.

        Parameter:
            prompt (str): The prompt message to display.
            regex_pattern (str): The regular expression pattern to validate the input (optional).
            error_message (str): Error message if the input is invalid.

        Return:
            (str): The valid input from the user.        
        """
        
        while True:
            value = input(prompt)
            if regex_pattern:
                if re.match(regex_pattern, value):
                    return value
                else:
                    logger.info(error_message)
            else:
                if value.strip():
                    return value
                else:
                    logger.info("Input cannot be empty. Please try again.")

    def add_contact(self, multiple=False):

        """
        Description:
            Adds one or more contacts to the address book.

        Parameter:
            self:Instance of the class
            multiple (bool): If True, the method will allow adding multiple contacts.

        Return:
            None
        """

        while True:
            first_name = self.get_valid_input("First Name: ", r'[A-Za-z]{3,}$', "Invalid Name. Enter at least a 3-letter name")
            last_name = self.get_valid_input("Last Name: ", r'[A-Za-z]{3,}$', "Invalid Name. Enter at least a 3-letter name")
            address = self.get_valid_input("Address: ")
            city = self.get_valid_input("City: ")
            state = self.get_valid_input("State: ")
            zip_code = self.get_valid_input("ZIP Code: ", r'^\d{6}$', "Invalid ZIP Code. Please enter a 6-digit number.")
            phone_number = self.get_valid_input("Phone Number: ", r'^\d{10}$', "Invalid Phone Number. Please enter a 10-digit number.")
            email = self.get_valid_input("Email: ", r'^\w+@\w+\.\w+$', "Invalid Email. Please enter a valid email address.")

            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            self.contacts.append(contact)
            logger.info(f"Contact {first_name} {last_name} added successfully.")

            if not multiple:
                break
            more = input("Do you want to add another contact? (yes/no): ").strip().lower()
            if more != 'yes':
                break

    def find_contact(self, first_name, last_name):

        """
        Description:
            Finds a contact by first and last name.

        Parameter:
            self:Instance of the class
            first_name(str): first name to check in contact 
            last_name(str): last name to check in contact

        Return:
            None                
        """

        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                return contact
        logger.info(f"Contact {first_name} {last_name} not found.")
        return None

    def delete_contact(self, first_name, last_name):

        """
        Description:
            Deletes a contact by first and last name.

        Parameter:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.

        Return:
            None
        """

        contact = self.find_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            logger.info(f"Contact {first_name} {last_name} deleted successfully.")
        else:
            logger.info(f"Contact {first_name} {last_name} not found.")

    def edit_contact(self, first_name, last_name):

        """
        Description:
            Edits an existing contact by searching with the name.

        Parameter:
            first_name:based on first name will edit contact 
            last_name:based on last name will edit contact  

        Return:
            None          
        """

        contact = self.find_contact(first_name, last_name)
        if contact:
            print("Editing contact details. Leave blank to keep current value.")
            new_first_name = self.get_valid_input(f"First Name ({contact.first_name}): ") or contact.first_name
            new_last_name = self.get_valid_input(f"Last Name ({contact.last_name}): ") or contact.last_name
            new_address = self.get_valid_input(f"Address ({contact.address}): ") or contact.address
            new_city = self.get_valid_input(f"City ({contact.city}): ") or contact.city
            new_state = self.get_valid_input(f"State ({contact.state}): ") or contact.state
            new_zip_code = self.get_valid_input(f"ZIP Code ({contact.zip_code}): ", r'^\d{6}$', "Invalid ZIP Code.") or contact.zip_code
            new_phone_number = self.get_valid_input(f"Phone Number ({contact.phone_number}): ", r'^\d{10}$', "Invalid Phone Number.") or contact.phone_number
            new_email = self.get_valid_input(f"Email ({contact.email}): ", r'^\w+@\w+\.\w+$', "Invalid Email.") or contact.email

            contact.update_contact(
                first_name=new_first_name,
                last_name=new_last_name,
                address=new_address,
                city=new_city,
                state=new_state,
                zip_code=new_zip_code,
                phone_number=new_phone_number,
                email=new_email
            )
        else:
            logger.info(f"Contact {first_name} {last_name} does not exist.")

    def display_contacts(self):

        """
        Description:
            Displays all the contacts in the address book.

        Parameter:
            self:Instance of class

        Return:
            None                
        """

        if not self.contacts:
            print(f"No contacts found in {self.name} Address Book.")
        for contact in self.contacts:
            contact.display()


class AddressBookSystem:

    def __init__(self):
        self.address_books = {}

    def create_address_book(self, name):

        """
        Description:
            Creates a new address book with a unique name.

        Parameter:
            self:Instance of the class
            name:name of the address book needs to be created

        Return:
            None              
        """

        if name in self.address_books:
            logger.info(f"Address book with name {name} already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            logger.info(f"Address book {name} created successfully.")

    def select_address_book(self):

        """
        Description:
            Selects an existing address book by name.

        Parameter:
            self:Instance of the class

        Return:
            None               
        """

        if not self.address_books:
            print("No address books available.")
            return None

        print("\nAvailable Address Books:")
        for name in self.address_books:
            print(f"- {name}")
        
        name = input("Enter the name of the address book to select: ")
        return self.address_books.get(name)


def main():
    try:
        system = AddressBookSystem()
        while True:
            print("\n1. Create Address Book\n2. Select Address Book\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter a unique name for the new address book: ")
                system.create_address_book(name)

            elif choice == '2':
                selected_book = system.select_address_book()
                if selected_book:
                    while True:
                        print(f"\nAddress Book: {selected_book.name}")
                        print("1. Add Single Contact\n2. Add Multiple Contacts\n3. Edit Contact\n4. Delete Contact\n5. Display Contacts\n6. Go Back")
                        book_choice = input("Choose an option: ")

                        if book_choice == '1':
                            selected_book.add_contact()
                        elif book_choice == '2':
                            selected_book.add_contact(multiple=True)
                        elif book_choice == '3':
                            first_name = input("Enter the first name of the contact to edit: ")
                            last_name = input("Enter the last name of the contact to edit: ")
                            selected_book.edit_contact(first_name, last_name)
                        elif book_choice == '4':
                            first_name = input("Enter the first name of the contact to delete: ")
                            last_name = input("Enter the last name of the contact to delete: ")
                            selected_book.delete_contact(first_name, last_name)
                        elif book_choice == '5':
                            selected_book.display_contacts()
                        elif book_choice == '6':
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
