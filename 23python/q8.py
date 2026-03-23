#8. Create a contact book using a dictionary with options to add, search, delete, and list contacts.
contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
    else:
        print("Not found")

def list_contacts():
    for name, phone in contacts.items():
        print(name, ":", phone)

while True:
    print("\n1.Add 2.Search 3.Delete 4.List 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        list_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice")