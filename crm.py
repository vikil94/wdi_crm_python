
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
        contact = Contact.create(first_name=first_name, last_name=last_name, email=email, note=note)
        # contact = Contact.create(first_name, last_name, email, note)

        # call the appropriate method from the contact class (remember we imported it?):

        # Contact.create(first_name, last_name, email, note)

    def modify_existing_contact(self):
        """As a user, if I select modify I am prompted to enter an id for the contact to be modified.
        As a user, when I enter the id of the user I want to modify I am then prompted to select which attribute I want to change from the list 'first name', 'last name', 'email', or 'note'.
        As a user, when I enter the attribute I want to change I am then prompted to enter a new value for the attribute."""

        print("Enter the id of the contact you would like to modify")
        user_input = int(input())

        print("Which part of the contact would you like to change?")
        print("first_name")
        print("last_name")
        print("email")
        print("note")
        print("Enter your input")
        attribute_input = input()

        print("Enter in the new value of this contact")
        value_input = input()

        updated_contact = Contact.get(id=user_input)

        updated_contact.update(attribute_input, value_input)

        print("You have updated your contact information")

    def delete_contact(self):
        """As a user, if I select delete I am then prompted to enter the id of the contact I want to delete."""

        print("Enter the id of the contact you want to delete")
        user_input = int(input())
        this_contact = Contact.get(id=user_input)
        this_contact.delete()
        print("Contact has been deleted")

    def display_all_contacts(self):
        """As a user, if I select display all I am then shown all of the contacts that exist."""

        print("These are all the contacts:")
        for i in Contact.select():
            print(i.full_name())

    def search_by_attribute(self):
        """As a user, if search by attribute is selected, I am prompted to select which attribute I want to search byself.
        As a user, when I choose which attribute I want to search by, I am then prompted to enter the search term.
        As a user, when I enter the search term I am then presented with the first contact who matches my search."""

        print("What attribute would you like to search by?")
        print("[1] First Name")
        print("[2] Last Name")
        print("[3] Email Address")
        print("[4] Notes")
        attribute = int(input())
        print("What value would you like to search by?")
        value = input()
        if attribute == 1:
            output = Contact.get(first_name=value)
        elif attribute == 2:
            output = Contact.get(last_name=value)
        elif attribute == 3:
            output = Contact.find_by(email=value)
        elif attribute == 4:
            output = Contact.find_by(note=value)
        if output is not False:
            print("Here is your contact")
            print("{} {}, Email Address: {}, Note: {}".format(output.first_name, output.last_name, output.email, output.note))


a_crm_app = CRM()
a_crm_app.main_menu()
