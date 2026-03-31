contacts = []
def add_contact(name, phone):
    contacts.append({'name': name, 'phone': phone})
    print(f'Contact {name} added successfully')

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")  
view_contacts()
