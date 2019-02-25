
from contact import Contact


class CRM:

    def main_menu(self):
        while True:  # repeat indefinitely
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            quit()
        else:
            return "Not an option"

    def add_new_contact(self):
        # get all the required info from our user:
        print('Enter First Name: ')
        first_name = input()

        print('Enter Last Name: ')
        last_name = input()

        print('Enter Email Address: ')
        email = input()

        print('Enter a Note: ')
        note = input()
        # call the appropriate method from the contact class (remember we imported it?):
        Contact.create(first_name, last_name, email, note)

        # call the appropriate method from the contact class (remember we imported it?):

        Contact.create(first_name, last_name, email, note)

    def modify_existing_contact(self):
        """As a user, if I select modify I am prompted to enter an id for the contact to be modified.
        As a user, when I enter the id of the user I want to modify I am then prompted to select which attribute I want to change from the list 'first name', 'last name', 'email', or 'note'.
        As a user, when I enter the attribute I want to change I am then prompted to enter a new value for the attribute."""

        print("Enter the id of the contact you would like to modify")
        user_input = int(input())
        print("Which part of the contact would you like to change?")
        print("[1] - First Name")
        print("[2] - Last Name")
        print("[3] - Email Address")
        print("[4] - Note")
        attribute_input = int(input())
        print("Enter in the new value of this contact")
        value = input()
        updated_contact = Contact.find(user_input)
        if attribute_input == 1:
            updated_contact.update('first_name', value)
        elif attribute_input == 2:
            updated_contact.update('last_name', value)
        elif attribute_input == 3:
            updated_contact.update('email', value)
        elif attribute_input == 4:
            updated_contact.update('note', value)

        print("You have updated your contact information")

    def delete_contact(self):
        """As a user, if I select delete I am then prompted to enter the id of the contact I want to delete."""

        print("Enter the id of the contact you want to delete")
        user_input = int(input())
        this_contact = Contact.find(user_input)
        this_contact.delete()
        print("Contact has been deleted")

    def display_all_contacts(self):
        """As a user, if I select display all I am then shown all of the contacts that exist."""
        Contact.all()

    def search_by_attribute(self):
        """As a user, if search by attribute is selected, I am prompted to select which attribute I want to search byself.
        As a user, when I choose which attribute I want to search by, I am then prompted to enter the search term.
        As a user, when I enter the search term I am then presented with the first contact who matches my search."""

        print("Which attribute would you like to search by?")
        print("[1] - First Name")
        print("[2] - Last Name")
        print("[3] - Email Address")
        print("[4] - Note")
        user_input = int(input())
        print("Enter in the value of what you are searching for")
        value = input()
        if user_input == 1:
            output = Contact.find_by('first_name', value)
        elif user_input == 2:
            output = Contact.find_by('last_name', value)
        elif user_input == 3:
            output = Contact.find_by('email', value)
        elif user_input == 4:
            output = Contact.find_by('note', value)

        print("Here is the information: {}".format(output))


a_crm_app = CRM()
a_crm_app.main_menu()
