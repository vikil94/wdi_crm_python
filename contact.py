class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        """This method should initialize the contact's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        # assign new contact's id attribute using value of class variable
        self.id = Contact.next_id
        # increment class variable, so the next contact that gets made will
        # have a different id
        Contact.next_id += 1

    @classmethod
    def create(cls, first_name, last_name, email, note):
        """This method should call the initializer,
    store the newly created contact, and then return it
    """
        new_person = Contact(first_name, last_name, email, note)
        cls.contacts.append(new_person)
        return new_person

    @classmethod
    def all(cls):
        """This method should return all of the existing contacts"""
        return cls.contacts

    @classmethod
    def find(cls, user_input):
        """ This method should accept an id as an argument
    and return the contact who has that id
    """
    # this method works
        for i in range(0, len(cls.contacts)):
            if cls.contacts[i].id == user_input:
                return cls.contacts[i]
            else:
                return "Contact not found"

    def update(self, attribute, value):
        """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """

        if attribute not in ['first_name', 'last_name', 'email', 'note']:
            return False
        elif attribute == 'first_name':
            self.first_name = value
        elif attribute == 'last_name':
            self.last_name = value
        elif attribute == 'email':
            self.last_name = value
        elif attribute == 'note':
            self.note = value
        else:
            return False

    @classmethod
    def find_by(cls):
        """This method should work similarly to the find method above but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact
    named Betty
        """

        for i in range(0, len(cls.contacts)):
            this_contact = cls.contacts[i]
            

    @classmethod
    def delete_all(cls):
        """This method should delete all of the contacts"""
        cls.contacts.clear()

    def full_name(self):
        """Returns the full (first and last) name of the contact"""

    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """

        # Feel free to add other methods here, if you need them.


# contact1 = Contact('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
# print(contact1)
contact1 = Contact.create('Betty', 'Maker', 'bettymakes@bitmakerlabs.com', 'Loves Pokemon')
contact2 = Contact.create('Bit', 'Bot', 'bitbot@bitmakerlabs.com', 'beep boop')

print(len(Contact.contacts))
print(contact1.id)
print(contact2.id)
print(Contact.find(1))
print(Contact.find(5))
print(contact1.first_name)
contact1.update('first_name', 'Vikil')
print(contact1.first_name)
print(contact2.note)
contact2.update('note', 'Loves animals')
print(contact2.note)
