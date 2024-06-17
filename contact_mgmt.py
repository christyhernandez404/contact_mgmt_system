import time
import re
import os

contact_book = {
    1: {"Name": 'Beyonce', "Phone Number": '987-345-1234', "Email": 'beyonce@gmail.com', "Address": '1105 NE 144ST, North Miami, FL, 33161', "Notes": 'South Florida House'},
    2: {"Name": 'Ulysses', "Phone Number": '305-345-9898', "Email": 'ulysses@gmail.com', "Address": "Valeria's House", "Notes": 'NA'}
}


def add_contact():
    while True:
        name = input("Enter name: ")
        phone_number_valid = False
        while not phone_number_valid:
            phone_number = input("Enter phone number: ")
            phone_number_valid = validate_phone(phone_number)
            if not phone_number_valid:
                print("Invalid phone number. Try again")
        email_valid = False
        while not email_valid:
            email = input(
                "Enter email address. If applicable, type NA: ").lower()
            email_valid = validate_email(email)
            if not email_valid:
                print("Invalid email. Try again")
        address = input("Enter address. If applicable, type NA: ")
        notes = input("Enter notes. If not applicable, type NA: ")
        print(f"Name: {name}, Phone Number: {phone_number}, Email: {
              email}, Address: {address}, Notes: {notes}")
        correct = input("Is this information accurate? y/n ")
        if correct.lower() == 'y':
            new_id = max(contact_book.keys()) + 1
            contact_book[new_id] = {'Name': name, 'Phone Number': phone_number,
                                    'Email': email, 'Address': address, 'Notes': notes}
            break
        else:
            continue


def validate_phone(phone_number):
    match = re.fullmatch(r"\(?\d{3}(\s|-|\))?\d{3}(\s|-)?\d{4}", phone_number)
    return bool(match)


def validate_email(email):
    match = re.fullmatch(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
    return bool(match)


def edit_contact():
    try:
        search_name = input("Type in the name you'd like to edit: ").lower()
        found_contact = False
        for contact_id, contact_info in contact_book.items():
            if search_name in contact_info['Name'].lower():
                found_contact = True
                what_to_edit = input(
                    "Type in what you'd like to edit about the contact. Name, phone number, email, address or notes: ").lower()
                if contact_id in contact_book and what_to_edit == 'name'.strip():
                    edit_name = input("Input new name: ")
                    contact_book[contact_id]['Name'] = edit_name
                elif contact_id in contact_book and what_to_edit == 'phone number':
                    phone_number_valid = False
                    while not phone_number_valid: # this loop will keep running until a phone number is valid
                        edit_phone_number = input("Input new phone number: ")
                        phone_number_valid = validate_phone(edit_phone_number) #this only flips to True if  the boolean in the validate_phone function
                        if phone_number_valid:
                            contact_book[contact_id]['Phone Number'] = edit_phone_number
                        else:
                            print("Invalid phone number. Try again.")
                elif contact_id in contact_book and what_to_edit == 'email':
                    email_valid = False
                    while not email_valid: # this loop will keep running until an email is valid
                        edit_email = input("Input new email: ")
                        if edit_email.lower() != "na":
                            email_valid = validate_email(edit_email) #this only flips to True if  the boolean in the validate_email function
                            if email_valid:
                                contact_book[contact_id]['Email'] = edit_email
                            else:
                                print("Invalid email. Try again.")
                        else:
                            email_valid = True
                            contact_book[contact_id]['Email'] = "NA"
                elif contact_id in contact_book and what_to_edit == 'address':
                    edit_address = input("Input new address: ")
                    contact_book[contact_id]['Address'] = edit_address
                elif contact_id in contact_book and what_to_edit == 'notes':
                    edit_notes = input("Input new notes: ")
                    contact_book[contact_id]['Notes'] = edit_notes
                else:
                    if contact_id not in contact_book:
                        print("Invalid name")
                print(f"The contact has been updated: ID: {contact_id}, Name: {contact_book[contact_id]['Name']}, Phone Number: {contact_book[contact_id]['Phone Number']},'Email': {contact_book[contact_id]['Email']}, 'Address': {contact_book[contact_id]['Address']}, 'Notes': {contact_book[contact_id]['Notes']}")
        if not found_contact:
            print("Contact not found")
    except Exception as e:
        print(f"An error occurred: {e}")



def delete_contact():
    search_name = input("Type in the name you'd like to delete: ").lower()
    found_contact = False
    contact_book_copy = contact_book.copy()  
    for contact_id, contact_info in contact_book_copy.items():
        if search_name in contact_info['Name'].lower():
            confirm = input(
                f"Please confirm you'd like to delete the contact '{contact_info['Name']}': y/n ").lower()
            if confirm == 'y':
                name_to_delete = contact_info['Name']
                # Delete from the original dictionary
                del contact_book[contact_id]
                print(f"Contact '{name_to_delete}' has been deleted")
                found_contact = True
            else:
                print("Deletion cancelled")
    if not found_contact:
        print("Contact not found")


def display_all_contacts():
    print("Here are your contacts:")
    for contact_id, contact_info in contact_book.items():
        print(f"ID: {contact_id}, Name: {
            contact_info['Name']}, Phone Number: {contact_info['Phone Number']}, Email: {contact_info['Email']}, Address: {contact_info['Email']}, Notes: {contact_info['Notes']} ")


def search_contact():
    search = input("Input the name you'd like to search: ").lower()
    found_contacts = False
    for contact_id, contact_info in contact_book.items():
        if search in contact_info['Name'].lower():
            print(f"ID: {contact_id}, Name: {contact_info['Name']}, Phone Number: {contact_info['Phone Number']}, Email: {
                  contact_info['Email']}, Address: {contact_info['Email']}, Notes: {contact_info['Notes']} ")
            found_contacts = True
        if not found_contacts:  # this means if found_contracts remains False
            print('Contact not found.')


def export_contacts(filename='contacts.txt'):
    try:
        with open(filename, 'w') as file:
            for contact_id, contact_info in contact_book.items():
                file.write(f"ID: {contact_id}\n")
                file.write(f"Name: {contact_info['Name']}\n")
                file.write(f"Phone Number: {contact_info['Phone Number']}\n")
                file.write(f"Email: {contact_info['Email']}\n")
                file.write(f"Address: {contact_info['Address']}\n")
                file.write(f"Notes: {contact_info['Notes']}\n")
                file.write("\n")  # Add newline for readability between contacts
        print(f"Contacts have been exported to {filename}")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")


def import_contacts(file):
    try:
        with open('new_file.txt', 'r') as file:
            lines = file.readlines()  
            contact_id = max(contact_book.keys()) + 1
            contact_info = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Name:"):
                    contact_info['Name'] = line.split("Name: ")[1]
                elif line.startswith("Phone Number:"):
                    contact_info['Phone Number'] = line.split("Phone Number: ")[
                        1]
                elif line.startswith("Email:"):
                    contact_info['Email'] = line.split("Email: ")[1]
                elif line.startswith("Address:"):
                    contact_info['Address'] = line.split("Address: ")[1]
                elif line.startswith("Notes:"):
                    contact_info['Notes'] = line.split("Notes: ")[1]

                if 'Name' in contact_info and 'Phone Number' in contact_info and 'Email' in contact_info and 'Address' in contact_info and 'Notes' in contact_info:
                    contact_book[contact_id] = contact_info
                    contact_id += 1  # Increment for the next contact
                    contact_info = {}  # Reset contact_info for the next contact
                    print(f"Contacts have been imported!")
    except Exception as e:
        print(f"The following error occurred while importing contacts: {e}")


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    while True:
        ans = input("""
Welcome to the Contacts app!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file
8. Quit

Enter the corresponding number for the action you'd like to take here: """)
        if ans == '1':
            add_contact()
            clear()
        elif ans == '2':
            edit_contact()
        elif ans == '3':
            delete_contact()
            time.sleep(6)
            clear()
        elif ans == '4':
            search_contact()
            time.sleep(6)
            clear()
        elif ans == '5':
            display_all_contacts()
            time.sleep(6)
            clear()
        elif ans == '6':
            export_contacts()
            time.sleep(6)
            clear()
        elif ans == '7':
            import_contacts('new_file.txt')
            time.sleep(7)
            clear()
        elif ans == '8':
            print("Thanks for using the Contacts app!")
            break
        else:
            print("Invalid data entry. Try again")



main()
