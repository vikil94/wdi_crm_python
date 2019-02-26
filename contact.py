from peewee import SqliteDatabase, Model, CharField, TextField

db = SqliteDatabase('crm.db')


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    class Meta:
        database = db  # db is the SqliteDatabase instance we made above

        def full_name(self):
            """Returns the full (first and last) name of the contact"""
            return self.first_name + " " + self.last_name


# this goes outside the class
db.connect()
db.create_tables([Contact])

Contact.create(first_name='Betty', last_name='Maker', email='bettymakes@bitmaker.co', note='this is a note')
Contact.create(first_name='Vikil', last_name='Naik', email='blah', note='whats up')
