from contact.contact import Contact

class Contact_manager():

    def __init__(self):
        self.contact_list = []

    def look_up(self):
        lname = input("Enter a name: ")
        found = False

        for contact in self.contact_list:
            if lname == contact.name:
                found = True
                print(str(contact))
                break

        if not found:
            print("Name not found")

    def new_contact(self):

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        person =  Contact(name, phone, email)
        self.contact_list.append(person)

        print("The entry has been added")

    def change_contact(self):
        cname = input("Enter a name: ")

        for contact in self.contact_list:
            if cname == contact.name:
                self.delete_contact(cname)
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")

                person = Contact(name, phone, email)
                self.contact_list.append(person)

    def delete_contact(self):
        dname = input("Enter a name: ")

        for contact in self.contact_list:
            if dname == contact.name:
                delete_contact = contact

        self.contact_list.remove(delete_contact)

    def case(self):

        while True:
            print("Menu")
            print("-" * 20)
            print("1. Look up a contact")
            print("2. Add a new contact")
            print("3. Change an existing contact")
            print("4. Delete a contact")
            print("5. Quit the program")

            self.number = int(input("Enter your choise: "))

            if self.number == 1:
                self.look_up()
            elif self.number == 2:
                self.new_contact()
            elif self.number == 3:
                self.change_contact()
            elif self.number == 4:
                self.delete_contact()
            elif self.number == 5:
                break
