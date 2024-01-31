rcontact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print(f"{key}\t\t{contact.get(key)}")

while True:
    choice = int(input("1. Add Contact \n 2. Search Contact \n 3. View Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit \n 7.Your Choice: "))

    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contact[name] = phone

    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(f"{search_name}'s, name contact number is, {contact[search_name]}")
        else:
            print("The contact is not found.")

    elif choice == 3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()

    elif choice == 4:
        modify_contact = input("Enter the contact name to be edited: ")
        if modify_contact in contact:
            new_phone = input("Enter the number to be updated: ")
            contact[modify_contact] = new_phone
            print("Number updated.")
            display_contact()
        else:
            print("The name is not present in the contact book.")

    elif choice == 5:
        del_contact = input("Enter the contact name to be deleted: ")
        if del_contact in contact:
            confirm = input("Are you sure you wish to delete the contact? - Y/N \n")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
                print("The contact has been deleted successfully.")
            display_contact()
        else:
            print("The contact is not found.")

    elif choice == 6:
        break

    else:
        print("Invalid Option. Please select the correct option.")


